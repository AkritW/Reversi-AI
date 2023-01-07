# built-in import
from typing import TypedDict, Tuple, List
from enum import Enum

# external import
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np

# internal import
from reversi import Reversi


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "localhost:5173",
    ],
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


class ReversiGameState(TypedDict):
    board: List[List[int]]
    player: int
    blackScore: int
    whiteScore: int


@app.get("/board")
async def get_board() -> ReversiGameState:
    board = [[int(e) for e in r] for r in reversi.board]
    valid_board = [[int(e) for e in r] for r in reversi.get_valid_board()]
    for y, _ in enumerate(valid_board):
        for x, _ in enumerate(valid_board[y]):
            if board[y][x] == -1:
                board[y][x] = 2
            if valid_board[y][x] == 1:
                board[y][x] = 3

    return {
        "board": board,
        "player": reversi.player,
        "blackScore": reversi.ai_disk_count,
        "whiteScore": reversi.player_disk_count,
    }


class Player(Enum):
    AI: 0
    USER: 1


class PlaceInformation(TypedDict):
    player: int
    locs: List[int]


@app.post("/place")
async def place_to_board(
    place_information: PlaceInformation,
) -> ReversiGameState:
    reversi.place_inplace(
        place_information["player"], place_information["locs"]
    )
    if reversi.game_is_ended():
        reversi.reset()
    board = [[int(e) for e in r] for r in reversi.board]
    valid_board = [[int(e) for e in r] for r in reversi.get_valid_board()]
    for y, _ in enumerate(valid_board):
        for x, _ in enumerate(valid_board[y]):
            if board[y][x] == -1:
                board[y][x] = 2
            if valid_board[y][x] == 1:
                board[y][x] = 3

    return {
        "board": board,
        "player": reversi.player,
        "blackScore": reversi.ai_disk_count,
        "whiteScore": reversi.player_disk_count,
    }
