import sys
sys.path.append('/Users/allisonhonold/ds0805/advent_of_code')

from day_5.day5_pt2 import get_input
import numpy as np
from intcode13_2 import IntcodeComp
from d13 import chunks
from matplotlib import pyplot as plt


class BrickBreaker():
    def __init__(self):
        self.board = np.zeros((40,40), dtype='int8')
        self.score = 0
        self.ball_x = None
        self.paddle_x = None

    def mark_tile(self, x, y, tile_id):
        """marks the tile at given location with tile_id (0=empty, 1=wall,
        2=block, 3=paddle, 4=ball)
        """
        self.board[y, x] = tile_id
        if tile_id == 4:
            self.ball_x = x
        if tile_id == 3:
            self.paddle_x = x

    def set_score(self, score):
        self.score = score

    def get_joystick(self):
        if (self.ball_x != None) and (self.paddle_x != None):
            if self.ball_x < self.paddle_x:
                return -1
            if self.ball_x > self.paddle_x:
                return 1
            if self.ball_x == self.paddle_x:
                return 0
        else:
            return 0

    def get_tile_count(self, tile_id):
        """returns the number of tiles with a given id"""
        tile_ids, counts = np.unique(self.board, return_counts=True)
        all_counts = dict(zip(tile_ids, counts))
        if tile_id in all_counts.keys():
            return all_counts[tile_id]
        else:
            return 0

    def display(self):
        plt.matshow(self.board)
        plt.show()



def main():
    # parse input
    input_code = get_input('input.txt')

    # play for free by setting memory address 0 to 2
    input_code[0] = 2

    # initialize game board
    board = BrickBreaker()

    # initalize intcode computer
    computer = IntcodeComp(input_code)

    # initialize joystic in neutral position
    joystick = 0

    while True:
        # board.display()

        # run computer and get outputs
        outputs = computer.compute(input_signal=joystick)

        for x, y, tile_id in chunks(outputs, 3):
            if x != -1:
                board.mark_tile(x, y, tile_id)
            elif x == -1 and y == 0:
                board.set_score(tile_id)

        joystick = board.get_joystick()

        # if no more blocks, break
        if board.get_tile_count(2) == 0:
            break

    # print the score
    print(board.score)


if __name__ == "__main__":
    main()

