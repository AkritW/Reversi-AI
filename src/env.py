"""
Reversi environment
"""

import numpy as np
import random
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete
from game import Reversi


class ReversiEnv(Env):
    def __init__(self):
        self.reversi = Reversi()
        self.action_space = Discrete(64)
        self.observation_space = Box(
            low=0, high=1, shape=self.encode_board3().shape, dtype=np.float64
        )
        self.episode_length = 0

    def encode_board1(self):
        # create a board with some mappings
        valid_board = self.reversi.get_valid_board()
        board1 = np.array(
            [
                [0.6666 if x == -1 else x for x in self.reversi.board[y]]
                for y, _ in enumerate(self.reversi.board)
            ]
        )
        for y, _ in enumerate(valid_board):
            for x, _ in enumerate(valid_board[y]):
                if valid_board[y, x] != 0:
                    board1[y, x] = 0.3333

        return np.append(board1.reshape(-1), self.reversi.player)

    def encode_board2(self):
        # create 2 board for player pieces and AI pieces
        board1 = np.array(
            [
                [1 if x == 1 else 0 for x in self.reversi.board[y]]
                for y, _ in enumerate(self.reversi.board)
            ]
        )
        board2 = np.array(
            [
                [1 if x == -1 else 0 for x in self.reversi.board[y]]
                for y, _ in enumerate(self.reversi.board)
            ]
        )

        return np.append(
            np.concatenate((board1, board2), axis=0).reshape(-1),
            self.reversi.player,
        )

    def encode_board3(self):
        # create 3 board for player pieces, AI pieces, and valid board
        board1 = np.array(
            [
                [1 if x == 1 else 0 for x in self.reversi.board[y]]
                for y, _ in enumerate(self.reversi.board)
            ]
        )
        board2 = np.array(
            [
                [1 if x == -1 else 0 for x in self.reversi.board[y]]
                for y, _ in enumerate(self.reversi.board)
            ]
        )
        board3 = self.reversi.get_valid_board()

        return np.append(
            np.concatenate((board1, board2, board3), axis=0).reshape(-1),
            self.reversi.player,
        )

    def step(self, action):
        self.episode_length += 1

        reward = 0
        disk_flipped = 1

        # get location of action
        place_location = (action // 8, action % 8)

        # get valid board
        valid_board = self.reversi.get_valid_board()

        # check for illegal move
        if valid_board[place_location] != 1:
            reward += -10
        else:
            # place board
            disk_flipped = self.reversi.place_inplace(
                self.reversi.player, place_location
            )

        # state of board after place
        state = self.encode_board3()

        # count reward
        reward += ((disk_flipped - 1) ** 2) * 10

        done = False

        # add more reward if done
        if self.reversi.game_is_ended():
            reward += 1000
            done = True
            # print("game is ended")

        # if self.episode_length > 5:
        #     print(self.reversi.board)
        #     print("reward", reward)
        #     print("episode_length", self.episode_length)
        #     print("done", done)
        #     print("\n\n")

        # info
        info = {}

        return state, reward, done, info

    def render(self):
        pass

    def reset(self):
        self.reversi.reset()
        self.episode_length = 0
        return self.encode_board3()


if __name__ == "__main__":
    env = ReversiEnv()
    print(check_env(env))
