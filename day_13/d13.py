import sys
sys.path.append('/Users/allisonhonold/ds0805/advent_of_code')

from day_5.day5_pt2 import get_input
import numpy as np
from intcode13 import IntcodeComp
from matplotlib import pyplot as plt

class BrickBreaker():
    def __init__(self):
        self.board = np.zeros((40,40), dtype='int8')

    def mark_tile(self, x, y, tile_id):
        """marks the tile at given location with tile_id (0=empty, 1=wall,
        2=block, 3=paddle, 4=ball)
        """
        self.board[y, x] = tile_id

    def get_tile_count(self, tile_id):
        """returns the number of tiles with a given id"""
        tile_ids, counts = np.unique(self.board, return_counts=True)
        all_counts = dict(zip(tile_ids, counts))
        return all_counts[tile_id]

    def display(self):
        plt.matshow(self.board)
        plt.show()


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



def main():
    # parse input
    input_code = get_input('input.txt')

    # initialize game board
    board = BrickBreaker()

    # initalize intcode computer
    computer = IntcodeComp(input_code)

    # run computer and get outputs
    outputs = computer.compute()

    # slice outputs into sets of three, adding a tile id for each set
    for x, y, tile_id in chunks(outputs, 3):
        board.mark_tile(x, y, tile_id)

    # print the number of block tiles (tile_id = 2)
    print(board.get_tile_count(2))

    # display board
    board.display()
    


    


if __name__ == "__main__":
    main()