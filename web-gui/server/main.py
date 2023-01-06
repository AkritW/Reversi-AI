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


@app.get("/board")
async def get_board() -> List[List[int]]:
    board = np.array([[e for e in row] for row in reversi.board])
    print(board)
    valid_board = reversi.get_valid_board()
    print(valid_board)
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if valid_board[i, j] != 0:
                board[i, j] = 2

    print(board)
    return board.tolist()


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
    reversi.place_inplace(place_information.player, place_information.locs)
    board = [[e for e in row] for row in reversi.board]
    valid_board = reversi.get_valid_board()
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if valid_board[i, j] != 0:
                board[i, j] = 2

    return board
