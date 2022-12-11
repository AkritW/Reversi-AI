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
        if player == Player.USER.value:
            pass
        else:
            pass

    def place(self, player, position):
        y, x = position
        self.board[y][x] = 1 if player == Player.USER.value else -1

        if player != self.player:
            return "It is not your turn!"

        # horizontally check left to right
        for i in range(1, x + 1, 1):
            print(x)
            if player == Player.USER.value:
                if self.board[y, x + i] == 0:
                    break
                elif self.board[y, x + i] == 1:
                    self.board[y, x : x + i] = [1 for _ in range(i)]
                elif self.board[y, x + 1] == -1:
                    pass
            elif player == Player.AI.value:
                if self.board[y, x + i] == 0:
                    break
                elif self.board[y, x + i] == -1:
                    self.board[y, x : x + i] = [-1 for _ in range(i)]
                elif self.board[y, x + 1] == 1:
                    pass

        # horizontal check right to left
        for i in range(1, 8 - x, 1):
            if player == Player.USER.value:
                if self.board[y, x - i] == 0:
                    break
                elif self.board[y, x - i] == 1:
                    self.board[y, x - i : x] = [1 for _ in range(i)]
                elif self.board[y, x - i] == -1:
                    pass
            elif player == Player.AI.value:
                if self.board[y][x - i] == 0:
                    break
                elif self.board[y, x - i] == -1:
                    self.board[y, x - i : x] = [-1 for _ in range(i)]
                elif self.board[y, x - i] == 1:
                    pass

        # vertical from top to bottom
        for i in range(1, 8 - y, 1):
            if player == Player.USER.value:
                if self.board[y + i, x] == 0:
                    break
                elif self.board[y + i, x] == 1:
                    self.board[y : y + i, x] = [1 for _ in range(i)]
                elif self.board[y + i, x] == -1:
                    pass
            elif player == Player.AI.value:
                if self.board[y + i, x] == 0:
                    break
                elif self.board[y][x] == -1:
                    self.board[y : y + 1, x] = [-1 for _ in range(i)]
                elif self.board[y + i, x] == 1:
                    pass

        # vertical from bottom to top
        for i in range(1, y + 1, 1):
            if player == Player.USER.value:
                if self.board[y - i, x] == 0:
                    break
                elif self.board[y - i, x] == 1:
                    self.board[y - i : y, x] = [1 for _ in range(i)]
                elif self.board[y - i, x] == -1:
                    pass
            elif player == Player.AI.value:
                if self.board[y - i, x] == 0:
                    break
                elif self.board[y, x] == -1:
                    self.board[y - i : y, x] = [-1 for _ in range(i)]
                elif self.board[y - i, x] == 1:
                    pass

        # # diagonally bottom right to upper left
        # for i in range(1, min(y, x), 1):
        #     if player == Player.USER.value:
        #         if self.board[y - i, x - i] == 0:
        #             break
        #         elif self.board[y - i, x - i] == 1:
        #             # self.board[y - i : y, x - i : x] = [1 for _ in range(i)]
        #             pass
        #         elif self.board[y - i, x] == -1:
        #             pass

        # change turn after one player has place
        self.next_turn()


if __name__ == "__main__":
    # For texting purposes

    reversi = Reversi()
    # print(reversi.player)
    # reversi.next_turn()
    # print(reversi.player)

    # print(reversi.board)

    # print(reversi.player)
    reversi.place(1, (4, 2))
    # reversi.place(0, (5, 4))
    # reversi.place(1, (3, 5))
    # reversi.place(0, (4, 1))
    # reversi.place(1, (6, 4))
    #   print(reversi.board[4:8, 2])
    # reversi.place(0, (0, 0))
    print(reversi.board)
