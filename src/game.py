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

        # track the number of disk for each player
        self.player_disk_count = 2
        self.ai_disk_count = 2

    def next_turn(self):
        self.player ^= 1

    def update_board(self, new_board):
        self.board = new_board

    def get_valid_position(self, player):
        valid_pos = []
        for y, _ in enumerate(self.board):
            for x, _ in enumerate(self.board[y]):
                if self.board[y, x] == 0:
                    if (
                        x != 7
                        and self.board[y, x + 1] != 0
                        and self.place(self.player, (y, x))[1] != 1
                    ):
                        valid_pos.append((y, x))
                    elif (
                        x != 0
                        and self.board[y, x - 1] != 0
                        and self.place(self.player, (y, x))[1] != 1
                    ):
                        valid_pos.append((y, x))
                    elif (
                        y != 7
                        and self.board[y + 1, x] != 0
                        and self.place(self.player, (y, x))[1] != 1
                    ):
                        valid_pos.append((y, x))
                    elif (
                        y != 0
                        and self.board[y - 1, x] != 0
                        and self.place(self.player, (y, x))[1] != 1
                    ):
                        valid_pos.append((y, x))
                    elif (
                        y != 7
                        and x != 7
                        and self.board[y + 1, x + 1] != 0
                        and self.place(self.player, (y, x))[1] != 1
                    ):
                        valid_pos.append((y, x))
                    elif (
                        y != 0
                        and x != 7
                        and self.board[y - 1, x + 1] != 0
                        and self.place(self.player, (y, x))[1] != 1
                    ):
                        valid_pos.append((y, x))
                    elif (
                        y != 7
                        and x != 0
                        and self.board[y + 1, x - 1] != 0
                        and self.place(self.player, (y, x))[1] != 1
                    ):
                        valid_pos.append((y, x))
                    elif (
                        y != 0
                        and x != 0
                        and self.board[y - 1, x - 1] != 0
                        and self.place(self.player, (y, x))[1] != 1
                    ):
                        valid_pos.append((y, x))

        return valid_pos

    def get_valid_board(self):
        valid_coords = self.get_valid_position(self.player)
        valid_board = np.array([[0 for _ in range(8)] for _ in range(8)])
        for coord in valid_coords:
            valid_board[coord[0], coord[1]] = 1
        return valid_board

    def fill_reverse_diagonal(self, board, disk):
        if len(board) != len(board[0]):
            raise ValueError("Board x and y is not the same size", board)

        y, x = 0, len(board[0]) - 1
        for _, _ in enumerate(board):
            board[y, x] = disk
            y += 1
            x -= 1

    def place(self, player, position):
        board = deepcopy(self.board)
        disk_flipped = 1

        if player != self.player:
            raise ValueError("It is not your turn!")

        if position[0] < 0 or position[1] < 0:
            raise ValueError("Position index can't be negative")

        y, x = position
        board[y, x] = 1 if player == Player.USER.value else -1

        # debugging purposes
        # print(y, x)
        # print(board)

        # horizontally check left to right
        for i in range(1, 8 - x, 1):
            if player == Player.USER.value:
                if board[y, x + i] == 0:
                    break
                elif board[y, x + i] == 1:
                    board[y, x : x + i + 1] = [1 for _ in range(i + 1)]
                    disk_flipped += i - 1
                    break
                elif board[y, x + 1] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y, x + i] == 0:
                    break
                elif board[y, x + i] == -1:
                    board[y, x : x + i + 1] = [-1 for _ in range(i + 1)]
                    disk_flipped += i - 1
                    break
                elif board[y, x + 1] == 1:
                    pass

        # horizontal check right to left
        for i in range(1, x + 1, 1):
            if player == Player.USER.value:
                if board[y, x - i] == 0:
                    break
                elif board[y, x - i] == 1:
                    board[y, x - i : x + 1] = [1 for _ in range(i + 1)]
                    disk_flipped += i - 1
                    break
                elif board[y, x - i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y][x - i] == 0:
                    break
                elif board[y, x - i] == -1:
                    board[y, x - i : x + 1] = [-1 for _ in range(i + 1)]
                    disk_flipped += i - 1
                    break
                elif board[y, x - i] == 1:
                    pass

        # vertical from top to bottom
        for i in range(1, 8 - y, 1):
            if player == Player.USER.value:
                if board[y + i, x] == 0:
                    break
                elif board[y + i, x] == 1:
                    board[y : y + i + 1, x] = [1 for _ in range(i + 1)]
                    disk_flipped += i - 1
                    break
                elif board[y + i, x] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y + i, x] == 0:
                    break
                elif board[y + i][x] == -1:
                    board[y : y + i + 1, x] = [-1 for _ in range(i + 1)]
                    disk_flipped += i - 1
                    break
                elif board[y + i, x] == 1:
                    pass

        # vertical from bottom to top
        for i in range(1, y + 1, 1):
            if player == Player.USER.value:
                if board[y - i, x] == 0:
                    break
                elif board[y - i, x] == 1:
                    board[y - i : y + 1, x] = [1 for _ in range(i + 1)]
                    disk_flipped += i - 1
                    break
                elif board[y - i, x] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y - i, x] == 0:
                    break
                elif board[y - i, x] == -1:
                    board[y - i : y + 1, x] = [-1 for _ in range(i + 1)]
                    disk_flipped += i - 1
                    break
                elif board[y - i, x] == 1:
                    pass

        # diagonally bottom right to upper left
        for i in range(1, min(y, x) + 1, 1):
            if player == Player.USER.value:
                if board[y - i, x - i] == 0:
                    break
                elif board[y - i, x - i] == 1:
                    np.fill_diagonal(board[y - i : y + 1, x - i : x + 1], 1)
                    disk_flipped += i - 1
                    break
                elif board[y - i, x - i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y - i, x - i] == 0:
                    break
                elif board[y - i, x - i] == -1:
                    np.fill_diagonal(board[y - i : y + 1, x - i : x + 1], -1)
                    disk_flipped += i - 1
                    break
                elif board[y - i, x - i] == 1:
                    pass

        # diagonally upper right to bottom left
        for i in range(1, min(8 - y, x + 1), 1):
            if player == Player.USER.value:
                if board[y + i, x - i] == 0:
                    break
                elif board[y + i, x - i] == 1:
                    self.fill_reverse_diagonal(
                        board[y : y + i + 1, x - i : x + 1], 1
                    )
                    disk_flipped += i - 1
                elif board[y + i, x - i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y + i, x - i] == 0:
                    break
                elif board[y + i, x - i] == -1:
                    self.fill_reverse_diagonal(
                        board[y : y + i + 1, x - i : x + 1], -1
                    )
                    disk_flipped += i - 1
                    break
                elif board[y + i, x - i] == 1:
                    pass

        # diagonally bottom left to upper right
        for i in range(1, min(y + 1, 8 - x), 1):
            if player == Player.USER.value:
                if board[y - i, x + i] == 0:
                    break
                elif board[y - i, x + i] == 1:
                    self.fill_reverse_diagonal(
                        board[y - i : y + 1, x : x + i + 1], 1
                    )
                    disk_flipped += i - 1
                    break
                elif board[y - i, x + i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y - i, x + i] == 0:
                    break
                elif board[y - i, x + i] == -1:
                    self.fill_reverse_diagonal(
                        board[y - i : y + 1, x : x + i + 1], -1
                    )
                    disk_flipped += i - 1
                    break
                elif board[y - i, x + i] == 1:
                    pass

        # diagonally upper left to bottom right
        for i in range(1, min(8 - y, 8 - x), 1):
            if player == Player.USER.value:
                if board[y + i, x + i] == 0:
                    break
                elif board[y + i, x + i] == 1:
                    np.fill_diagonal(board[y : y + i + 1, x : x + i + 1], 1)
                    break
                elif board[y + i, x + i] == -1:
                    pass
            elif player == Player.AI.value:
                if board[y + i, x + i] == 0:
                    break
                elif self.board[y + i, x + i] == -1:
                    np.fill_diagonal(board[y : y + i + 1, x : x + i + 1], -1)
                    break
                elif board[y + i, x + i] == 1:
                    pass

        return board, disk_flipped

    def place_inplace(self, player, location):
        # replace the board
        self.board, disk_flipped = self.place(player, location)

        # update disk_count
        if player == Player.AI:
            self.ai_disk_count += disk_flipped
            self.player_disk_count -= disk_flipped - 1
        elif player == Player.USER:
            self.player_disk_count += disk_flipped
            self.ai_disk_count -= disk_flipped - 1

        # change turn after one player has place
        self.next_turn()

        return disk_flipped

    def encode_board1(self):
        # create a board with some mappings
        valid_board = self.get_valid_board()
        board1 = np.array(
            [
                [0.6666 if x == -1 else x for x in self.board[y]]
                for y, _ in enumerate(self.board)
            ]
        )
        for y, _ in enumerate(valid_board):
            for x, _ in enumerate(valid_board[y]):
                if valid_board[y, x] != 0:
                    board1[y, x] = 0.3333

        return board1.reshape(-1)

    def encode_board2(self):
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

        return np.concatenate((board1, board2), axis=0).reshape(-1)

    def encode_board3(self):
        # create 3 board for player pieces, AI pieces, and valid board
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
        board3 = self.get_valid_board()

        return np.concatenate((board1, board2, board3), axis=0).reshape(-1)

    def game_is_ended(self):
        # one player can't place
        if len(self.get_valid_position(self.player)) == 0:
            return True

        # empty board
        for row in self.board:
            for e in row:
                if e == 0:
                    return False

        return True

    def reset(self):
        self.__init__()


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
    print(reversi.get_valid_board())
