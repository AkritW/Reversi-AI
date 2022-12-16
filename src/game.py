"""
Code for Reversi game engine
"""
from enum import Enum
from copy import deepcopy
import numpy as np


class Player(Enum):
    """Enum for type of players"""

    AI = 0
    USER = 1

    # In board, user = 1 and AI = -1


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
        valid_pos = []
        surrounding_dir = [
            [0, 1],
            [0, -1],
            [1, 0],
            [1, 1],
            [1, -1],
            [-1, 0],
            [-1, 1],
            [-1, -1],
        ]
        if player == Player.USER.value:
            for y in range(8):
                for x in range(8):
                    if self.board[y, x] == 0:
                        for dir in surrounding_dir:
                            if (
                                y + dir[0] > 7
                                or y + dir[0] < 0
                                or x + dir[1] < 0
                                or x + dir[1] > 7
                            ):
                                pass
                            else:
                                if self.board[y + dir[0], x + dir[1]] == -1:
                                    test_board = self.board.copy()
                                    test_board[y][x] = 1

                                    # horizontally check left to right
                                    for i in range(1, 7 - x, 1):

                                        if test_board[y, x + i] == 0:
                                            break
                                        elif test_board[y, x + i] == 1:
                                            test_board[y, x : x + i] = [
                                                1 for _ in range(i)
                                            ]
                                            break
                                        elif test_board[y, x + 1] == -1:
                                            pass

                                    # horizontal check right to left
                                    for i in range(1, x + 1, 1):

                                        if test_board[y, x - i] == 0:
                                            break
                                        elif test_board[y, x - i] == 1:
                                            test_board[y, x - i : x] = [
                                                1 for _ in range(i)
                                            ]
                                            break
                                        elif test_board[y, x - i] == -1:
                                            pass

                                    # vertical from top to bottom
                                    for i in range(1, 7 - y - 1, 1):

                                        if test_board[y + i, x] == 0:
                                            break
                                        elif test_board[y + i, x] == 1:
                                            test_board[y : y + i, x] = [
                                                1 for _ in range(i)
                                            ]
                                            break
                                        elif test_board[y + i, x] == -1:
                                            pass

                                    # vertical from bottom to top
                                    for i in range(1, y + 1, 1):

                                        if test_board[y - i, x] == 0:
                                            break
                                        elif test_board[y - i, x] == 1:
                                            test_board[y - i : y, x] = [
                                                1 for _ in range(i)
                                            ]
                                            break
                                        elif test_board[y - i, x] == -1:
                                            pass

                                    # diagonally bottom right to upper left
                                    for i in range(1, min(y, x) - 1, 1):

                                        if test_board[y - i, x - i] == 0:
                                            break
                                        elif test_board[y - i, x - i] == 1:
                                            np.fill_diagonal(
                                                test_board[
                                                    y - i : y, x - i : x
                                                ],
                                                1,
                                            )
                                            break
                                        elif test_board[y - i, x - i] == -1:
                                            pass

                                    # diagonally upper right to bottom left
                                    for i in range(i, min(7 - y, x), 1):

                                        if test_board[y + i, x - i] == 0:
                                            break
                                        elif test_board[y + i, x - i] == 1:
                                            self.fill_reverse_diagonal(
                                                test_board[
                                                    y : y + i,
                                                    x - i + 1 : x + 1,
                                                ],
                                                1,
                                            )
                                        elif test_board[y + i, x - i] == -1:
                                            pass

                                    # diagonally bottom left to upper right
                                    for i in range(i, min(y, 7 - x), 1):

                                        if test_board[y - i, x + i] == 0:
                                            break
                                        elif test_board[y - i, x + i] == 1:
                                            self.fill_reverse_diagonal(
                                                test_board[
                                                    y - i : y,
                                                    x - 1 : x + i + 1,
                                                ],
                                                1,
                                            )
                                            break
                                        elif test_board[y - i, x + i] == -1:
                                            pass

                                    # diagonally upper left to bottom right
                                    for i in range(i, min(7 - y, 7 - x), 1):

                                        if test_board[y + i, x + i] == 0:
                                            break
                                        elif test_board[y + i, x + i] == 1:
                                            np.fill_diagonal(
                                                test_board[
                                                    y : y + i, x : x + i
                                                ],
                                                1,
                                            )
                                            break
                                        elif test_board[y + i, x + i] == -1:
                                            pass

                                    if test_board.sum() > self.board.sum() + 1:
                                        # print([y,x])
                                        # print(test_board)
                                        valid_pos.append([y, x])
                                        break
                                    else:
                                        pass
                                else:
                                    pass
        else:
            for y in range(8):
                for x in range(8):
                    if self.board[y, x] == 0:
                        for dir in surrounding_dir:
                            if (
                                y + dir[0] > 7
                                or y + dir[0] < 0
                                or x + dir[1] < 0
                                or x + dir[1] > 7
                            ):
                                pass
                            else:
                                if self.board[y + dir[0], x + dir[1]] == 1:
                                    test_board = self.board.copy()
                                    test_board[y][x] = -1
                                    # horizontally check left to right
                                    for i in range(1, 7 - x, 1):

                                        if test_board[y, x + i] == 0:
                                            break
                                        elif test_board[y, x + i] == -1:
                                            test_board[y, x : x + i] = [
                                                -1 for _ in range(i)
                                            ]
                                            break
                                        elif test_board[y, x + 1] == 1:
                                            pass

                                    # horizontal check right to left
                                    for i in range(1, x + 1, 1):

                                        if test_board[y][x - i] == 0:
                                            break
                                        elif test_board[y, x - i] == -1:
                                            test_board[y, x - i : x] = [
                                                -1 for _ in range(i)
                                            ]
                                            break
                                        elif test_board[y, x - i] == 1:
                                            pass

                                    # vertical from top to bottom
                                    for i in range(1, 7 - y - 1, 1):

                                        if test_board[y + i, x] == 0:
                                            break
                                        elif test_board[y + i][x] == -1:
                                            test_board[y : y + i, x] = [
                                                -1 for _ in range(i)
                                            ]
                                            break
                                        elif test_board[y + i, x] == 1:
                                            pass

                                    # vertical from bottom to top
                                    for i in range(1, y + 1, 1):

                                        if test_board[y - i, x] == 0:
                                            break
                                        elif test_board[y - i, x] == -1:
                                            test_board[y - i : y, x] = [
                                                -1 for _ in range(i)
                                            ]
                                            break
                                        elif test_board[y - i, x] == 1:
                                            pass

                                    # diagonally bottom right to upper left
                                    for i in range(1, min(y, x) - 1, 1):

                                        if test_board[y - i, x - i] == 0:
                                            break
                                        elif test_board[y - i, x - i] == -1:
                                            np.fill_diagonal(
                                                test_board[
                                                    y - i : y, x - i : x
                                                ],
                                                -1,
                                            )
                                            break
                                        elif test_board[y - i, x - i] == 1:
                                            pass

                                    # diagonally upper right to bottom left
                                    for i in range(i, min(7 - y, x), 1):

                                        if test_board[y + i, x - i] == 0:
                                            break
                                        elif test_board[y + i, x - i] == -1:
                                            self.fill_reverse_diagonal(
                                                test_board[
                                                    y : y + i,
                                                    x - i + 1 : x + 1,
                                                ],
                                                -1,
                                            )
                                            break
                                        elif test_board[y + i, x - i] == 1:
                                            pass

                                    # diagonally bottom left to upper right
                                    for i in range(i, min(y, 7 - x), 1):

                                        if test_board[y - i, x + i] == 0:
                                            break
                                        elif test_board[y - i, x + i] == -1:
                                            self.fill_reverse_diagonal(
                                                test_board[
                                                    y - i : y,
                                                    x + 1 : x + i + 1,
                                                ],
                                                -1,
                                            )
                                            break
                                        elif test_board[y - i, x + i] == 1:
                                            pass

                                    # diagonally upper left to bottom right
                                    for i in range(i, min(7 - y, 7 - x), 1):

                                        if test_board[y + i, x + i] == 0:
                                            break
                                        elif test_board[y + i, x + i] == -1:
                                            np.fill_diagonal(
                                                test_board[
                                                    y : y + i, x : x + i
                                                ],
                                                -1,
                                            )
                                            break
                                        elif test_board[y + i, x + i] == 1:
                                            pass

                                    if test_board.sum() < self.board.sum() - 1:
                                        # print([y,x])
                                        valid_pos.append([y, x])
                                        break
                                    else:
                                        pass
                                else:
                                    pass

        return valid_pos

    def get_valid_board(self, player):
        valid_coords = self.get_valid_position(player)
        valid_board = np.array([[0 for _ in range(8)] for _ in range(8)])
        for coord in valid_coords:
            valid_board[coord[0], coord[1]] = 5
        return valid_board

    def fill_reverse_diagonal(self, board, disk):
        y, x = 0, len(board[0]) - 1
        for _ in range(min(len(board), 8 - len(board[0]))):
            board[y, x] = disk
            y += 1
            x -= 1

    def place(self, player, position):
        board = deepcopy(self.board)

        if player != self.player:
            return "It is not your turn!"

        y, x = position
        board[y, x] = 1 if player == Player.USER.value else -1

        # horizontally check left to right
        for i in range(1, 7 - x, 1):
            if player == Player.USER.value:
                if board[y, x + i] == 0:
                    break
                elif board[y, x + i] == 1:
                    board[y, x : x + i] = [1 for _ in range(i)]
                    break
                elif board[y, x + 1] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y, x + i] == 0:
                    break
                elif board[y, x + i] == -1:
                    board[y, x : x + i] = [-1 for _ in range(i)]
                    break
                elif board[y, x + 1] == 1:
                    pass

        # horizontal check right to left
        for i in range(1, x + 1, 1):
            if player == Player.USER.value:
                if board[y, x - i] == 0:
                    break
                elif board[y, x - i] == 1:
                    board[y, x - i : x] = [1 for _ in range(i)]
                    break
                elif board[y, x - i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y][x - i] == 0:
                    break
                elif board[y, x - i] == -1:
                    board[y, x - i : x] = [-1 for _ in range(i)]
                    break
                elif board[y, x - i] == 1:
                    pass

        # vertical from top to bottom
        for i in range(1, 7 - y - 1, 1):
            if player == Player.USER.value:
                if board[y + i, x] == 0:
                    break
                elif board[y + i, x] == 1:
                    board[y : y + i, x] = [1 for _ in range(i)]
                    break
                elif board[y + i, x] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y + i, x] == 0:
                    break
                elif board[y + i][x] == -1:
                    board[y : y + i, x] = [-1 for _ in range(i)]
                    break
                elif board[y + i, x] == 1:
                    pass

        # vertical from bottom to top
        for i in range(1, y + 1, 1):
            if player == Player.USER.value:
                if board[y - i, x] == 0:
                    break
                elif board[y - i, x] == 1:
                    board[y - i : y, x] = [1 for _ in range(i)]
                    break
                elif board[y - i, x] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y - i, x] == 0:
                    break
                elif board[y - i, x] == -1:
                    board[y - i : y, x] = [-1 for _ in range(i)]
                    break
                elif board[y - i, x] == 1:
                    pass

        # diagonally bottom right to upper left
        for i in range(1, min(y, x) - 1, 1):
            if player == Player.USER.value:
                if board[y - i, x - i] == 0:
                    break
                elif board[y - i, x - i] == 1:
                    np.fill_diagonal(self.board[y - i : y, x - i : x], 1)
                    break
                elif board[y - i, x - i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y - i, x - i] == 0:
                    break
                elif board[y - i, x - i] == -1:
                    np.fill_diagonal(self.board[y - i : y, x - i : x], -1)
                    break
                elif board[y - i, x - i] == 1:
                    pass

        # diagonally upper right to bottom left
        for i in range(i, min(7 - y, x), 1):
            if player == Player.USER.value:
                if board[y + i, x - i] == 0:
                    break
                elif board[y + i, x - i] == 1:
                    self.fill_reverse_diagonal(
                        board[y : y + i, x - i + 1 : x + 1], 1
                    )
                elif board[y + i, x - i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y + i, x - i] == 0:
                    break
                elif board[y + i, x - i] == -1:
                    self.fill_reverse_diagonal(
                        board[y : y + i, x - i + 1 : x + 1], -1
                    )
                    break
                elif board[y + i, x - i] == 1:
                    pass

        # diagonally bottom left to upper right
        for i in range(i, min(y, 7 - x), 1):
            if player == Player.USER.value:
                if board[y - i, x + i] == 0:
                    break
                elif board[y - i, x + i] == 1:
                    self.fill_reverse_diagonal(
                        board[y - i : y, x - 1 : x + i + 1], 1
                    )
                    break
                elif board[y - i, x + i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y - i, x + i] == 0:
                    break
                elif board[y - i, x + i] == -1:
                    self.fill_reverse_diagonal(
                        board[y - i : y, x + 1 : x + i + 1], -1
                    )
                    break
                elif board[y - i, x + i] == 1:
                    pass

        # diagonally upper left to bottom right
        for i in range(i, min(7 - y, 7 - x), 1):
            if player == Player.USER.value:
                if board[y + i, x + i] == 0:
                    break
                elif board[y + i, x + i] == 1:
                    np.fill_diagonal(board[y : y + i, x : x + i], 1)
                    break
                elif board[y + i, x + i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y + i, x + i] == 0:
                    break
                elif self.board[y + i, x + i] == -1:
                    np.fill_diagonal(board[y : y + i, x : x + i], -1)
                    break
                elif board[y + i, x + i] == 1:
                    pass

        return board

    def place_inplace(self, player, location):
        # replace the board
        self.board = self.place(player, location)
        # change turn after one player has place
        self.next_turn()

    def encode_board(self):
        # create 2 board for player pieces and AI pieces
        board1 = np.array(
            [
                [1 if x == 1 else 0 for x in self.board[y]]
                for y, _ in enumerate(self.board)
            ]
        )
        board2 = np.array(
            [
                [1 if x == -1 else 0 for x in self.board[y]]
                for y, _ in enumerate(self.board)
            ]
        )
        return board1, board2


if __name__ == "__main__":
    # For texting purposes

    reversi = Reversi()
    # print(reversi.player)
    # reversi.next_turn()
    # print(reversi.player)

    # print(reversi.board)

    # print(reversi.player)
    reversi.place_inplace(1, (2, 4))
    reversi.place_inplace(0, (4, 5))
    reversi.place_inplace(1, (5, 6))
    reversi.place_inplace(0, (1, 4))
    # reversi.place(1, (6, 4))
    # reversi.place(0, (4, 5))
    # reversi.place(1, (5, 3))
    # reversi.place(0, (7, 5))
    #   print(reversi.board[4:8, 2])
    # reversi.place(0, (0, 0))

    print(reversi.board)
    print(reversi.encode_board())

    print(reversi.get_valid_board(1))
