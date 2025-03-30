# Visibrain

A small application which offers the ability to fetch videos from a game using Twitch API, FastAPI, VueJS and MongoDB

## Missing features

* Settings from a file or the environment (probably using pydantic-settings)
* Tests
* User authentication

## How to start the application

1. Create an application on the [Twitch developer portal](https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/#client-credentials-grant-flow) and save the client_id and client_secret
2. Update the client_id and client_secret in back/main.py ligne 44 (they are currently set with ****** which is NOT a valid value)
3. Start the backend with `cd back && make run`
4. Start the fronted with `npm run dev`
