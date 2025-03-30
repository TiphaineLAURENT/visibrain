from http import HTTPStatus
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins="*")


async def twitch():
    return await Twitch('******', '******')

@app.get("/videos/")
async def videos(twitch: Annotated[Twitch, Depends(twitch)], game_name: str):
    game = await first(twitch.get_games(names=[game_name]))
    if not game:
        raise HTTPException(HTTPStatus.NOT_FOUND)

    return [video async for video in twitch.get_videos(game_id=game.id) if "404" not in video.thumbnail_url]
