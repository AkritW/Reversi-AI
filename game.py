"""
Code for Reversi game engine
"""
from enum import Enum
import numpy as np


class Player(Enum):
    """Enum for type of players"""

    AI = 0
    USER = 1


class Reversi:
    def __init__(self):
        # create a matrix and filled 4 disks in the middle
        self.board = np.array([[0 for _ in range(8)] for _ in range(8)])
        (
            self.board[3, 3],
            self.board[3, 4],
            self.board[4, 3],
            self.board[4, 4],
        ) = (1, -1, -1, 1)

        # assign the first player to be user
        self.player = Player.USER.value

    def next_turn(self):
        self.player ^= 1

    def update_board(self, new_board):
        self.board = new_board

    def get_valid_position(self, player):
        if player == player.USER.value:
            pass
        else:
            pass


if __name__ == "__main__":
    # For texting purposes

    reversi = Reversi()
    print(reversi.player)
    reversi.next_turn()
    print(reversi.player)

    print(reversi.board)
