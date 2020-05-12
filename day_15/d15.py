import sys
sys.path.append('/Users/allisonhonold/ds0805/advent_of_code')

from day_5.day5_pt2 import get_input
from intcode15 import IntcodeComp
import numpy as np
from matplotlib import pyplot as plt


wasHere = np.zeros((50, 50), dtype=bool)
correctPath = np.zeros((50,50), dtype=bool)
startX, startY = 25, 25
endX, endY = None, None

def get_neighbors(loc):
    x = loc[0]
    y = loc[1]
    neighbors = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
    return neighbors

def get_maze(computer, loc, maze):
    neighbors = get_neighbors(loc)

    for n in neighbors:
        if maze[n[1], n[0]] == 0:
            forward, back = direction(loc, n)
            status = computer.compute(forward)[0]
            if status == 0:
                maze[n[1], n[0]] = 2

            elif status == 1:
                maze[n[1], n[0]] = 1
                maze = get_maze(computer, n, maze)
                computer.compute(back)

            elif status == 2:
                maze[n[1], n[0]] = 3
                endX = n[0]
                endY = n[1]
                maze = get_maze(computer, n, maze)
                computer.compute(back)
    return maze
        

def direction(loc, n):
    if loc[0] == n[0]:
        if n[1] == loc[1] +1:
             return 1, 2
        else: return 2, 1
    else:
        if n[0] == loc[0] +1:
            return 4, 3
        else: return 3, 4


def solve_maze(maze):
    b = recursiveSolve(startX, startY, maze)
    return b

def recursiveSolve(x, y, maze):
    if x == endX and y == endY: return True
    if maze[y, x] == 2 or wasHere[y, x]: return False
    wasHere[y, x] = True
    if (recursiveSolve(x-1, y, maze) 
        or recursiveSolve(x+1, y, maze)
        or recursiveSolve(x, y-1, maze)
        or recursiveSolve(x, y+1, maze)):
        correctPath[y, x] = True
        return True
    return False


def main():
    # read input
    intcode = get_input('input.txt')

    # start IntCode computer
    comp = IntcodeComp(intcode)

    # get maze
    maze = np.zeros((50, 50))
    maze = get_maze(comp, [startX, startY], maze)


    # plt.matshow(maze)
    # plt.show()

    # solve maze
    solved = solve_maze(maze)

    plt.matshow(correctPath)
    plt.show()

    # return length of shortest path


if __name__ == "__main__":
    main()