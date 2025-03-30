# Visibrain

A small application which offers the ability to fetch videos from a game using Twitch API, FastAPI, VueJS and MongoDB

## Missing features

* Settings from a file or the environment (probably using pydantic-settings)
* Tests
* User authentication

## Installation

### Backend

1. Install docker : https://docs.docker.com/engine/install/ (for MongoDB)
2. `cd back`
3. `make init` (or manually install pyenv, pipx and poetry)
4. `poetry install --no-root`

### Frontend

1. Install `node>18` (I'm using [https://github.com/tj/n](n))
2. `npm install`

## How to start the application

1. Create an application on the [Twitch developer portal](https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/#client-credentials-grant-flow) and save the client_id and client_secret
2. Update the client_id and client_secret in back/main.py ligne 44 (they are currently set with ****** which is NOT a valid value)
3. Start the backend with `cd back && make run`
4. Start the fronted with `npm run dev`

## Screenshots

### Application at start

![application](https://github.com/user-attachments/assets/10efb658-cdec-4c41-9ae3-99f3b8406467)
![back logs](https://github.com/user-attachments/assets/943a6219-27e1-42b4-9d8e-335130ca1e36)
![front logs](https://github.com/user-attachments/assets/31e188c0-afca-4d8e-a10c-9072a9a03e19)

### In use example
![loading](https://github.com/user-attachments/assets/0ae1e38c-dab9-4114-838d-fec7e0459fee)
![loaded](https://github.com/user-attachments/assets/0e2029ff-c814-44d3-996c-1dc9afad226f)
