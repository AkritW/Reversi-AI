# built-in import
from typing import TypedDict, Tuple, List
from enum import Enum

# external import
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# internal import
from reversi import Reversi


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
reversi = Reversi()


class HelloWorldMessage(TypedDict):
    message: str


@app.get("/")
async def index() -> HelloWorldMessage:
    return {"message": "Hello World"}


@app.get("/board")
async def get_board() -> List[List[int]]:
    return reversi.board.tolist()


class Player(Enum):
    AI: 0
    USER: 1


class PlaceInformation(BaseModel):
    player: int
    locs: List[int]


@app.post("/place")
async def place_to_board(
    place_information: PlaceInformation,
) -> List[List[int]]:
    reversi.place(place_information.player, place_information.locs)
    return reversi.board.tolist()
