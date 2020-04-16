import sys
sys.path.append('/Users/allisonhonold/ds0805/advent_of_code')

from day_5.day5_pt2 import get_input
from intcode9 import IntcodeComp


def main():
    # read input
    puzzle_input = get_input('day9_input.txt')

    # create intcode computer
    comp = IntcodeComp(puzzle_input, 1)

    # run intcode computer
    print('BOOST keycode:')
    comp.compute()

    # create a new intcode computer for part 2 with input value 2
    comp2 = IntcodeComp(puzzle_input, 2)

    # run this intcode computer
    print('Distress signal coordinates:')
    comp2.compute()


if __name__ == "__main__":
    main()