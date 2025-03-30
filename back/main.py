import datetime
from http import HTTPStatus
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
from pymongo import MongoClient
from pydantic_mongo import AbstractRepository
from pydantic import BaseModel, ConfigDict, Field
import logging

logger = logging.getLogger("uvicorn")

class VideoMutedSegments(BaseModel):
    duration: int
    offset: int


class Video(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    title: str
    description: str
    url: str
    thumbnail_url: str
    viewable: str
    game_id: str | None = None
    saved_at: datetime.datetime | None = Field(default_factory=datetime.datetime.now)


class VideosRepository(AbstractRepository[Video]):
    class Meta:
        collection_name = "videos"


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins="*")


async def twitch():
    return await Twitch('******', '******')

client = MongoClient("mongodb://mongdb_username:mongdb_password@localhost:27017/")
database = client['visibrain']
videos_repository = VideosRepository(database)

logger.setLevel(logging.DEBUG)
logger.debug("Logging enabled")

@app.get("/videos/")
async def videos(twitch: Annotated[Twitch, Depends(twitch)], game_name: str) -> list[Video]:
    logger.debug("Fetching game info for name %s", game_name)
    game = await first(twitch.get_games(names=[game_name]))
    if not game:
        raise HTTPException(HTTPStatus.NOT_FOUND)
    logger.debug(game)

    logger.debug("Fetching recent videos from mongodb for game %s (%s)", game.id, game.name)
    saved_videos = list(videos_repository.find_by({"saved_at": {"$gte": datetime.datetime.now() - datetime.timedelta(minutes=2)}, "game_id": game.id}))
    if saved_videos:
        logger.debug("Found %s videos from mongodb", len(saved_videos))
        return saved_videos

    logger.debug("Found no recent videos from mongodb. Fetching from Twitch API")    
    api_videos = [Video.model_validate({**video.to_dict(), "game_id": game.id}) async for video in twitch.get_videos(game_id=game.id) if "404" not in video.thumbnail_url and video.viewable == "viewable"]
    logger.debug("Found %s videos from mongodb", len(api_videos))

    logger.debug("Saving %s videos in mongodb", len(api_videos))
    videos_repository.save_many(api_videos)
    logger.debug("%s videos saved", len(api_videos))
    return api_videos
