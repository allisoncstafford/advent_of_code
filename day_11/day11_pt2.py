import sys
sys.path.append('/Users/allisonhonold/ds0805/advent_of_code')

from day_5.day5_pt2 import get_input
from intcode11 import IntcodeComp
import numpy as np
from matplotlib import pyplot as plt

class Painter():
    def __init__(self):
        """establishes initial canvas, location, and direction. Location is 
        (x,y) where x increases left to right, y increases bottom to top
        """
        self.canvas = np.zeros((10, 10, 2), dtype=bool)
        self.loc = [5, 5]
        self.direction = 'up'
        # set starting color to white
        self.canvas[self.loc[0], self.loc[1], 0] = 1

    def get_count(self):
        count = 0
        for i in range(self.canvas.shape[0]):
            for j in range(self.canvas.shape[1]):
                count += self.canvas[i, j, 1]
        return count

    def move(self, turn_direction):
        if turn_direction == 0:
            self.turn_left()
        if turn_direction == 1:
            self.turn_right()
        self.step_forward()

    def turn_left(self):
        "Changes the direction of the painter for a left turn"
        if self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'up'

    def turn_right(self):
        "Changes the direction of the painter for a right turn"
        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'left':
            self.direction = 'up'
        elif self.direction == 'down':
            self.direction = 'left'
        elif self.direction == 'right':
            self.direction = 'down'

    def step_forward(self):
        "adjusts the location for a single step forward"
        canvas_shape = self.canvas.shape
        
        # if at edge of canvas, increase canvas size
        if (self.loc[0] in (1, canvas_shape[0]-2) 
            or self.loc[1] in (1, canvas_shape[1]-2)):
            self.expand_canvas()

        if self.direction == 'up':
            # increase location y by one
            self.loc[1] += 1

        if self.direction == 'left':
            # increase location y by one
            self.loc[0] -= 1

        if self.direction == 'down':
            # increase location y by one
            self.loc[1] -= 1

        if self.direction == 'right':
            # increase location y by one
            self.loc[0] += 1

    def expand_canvas(self):
        """expands the canvas by 10 in the direction where loc is within 1 of 
        the edge. adjusts loc to reflect the larger canvas if needed"""
        canvas_shape = self.canvas.shape
        # if loc at top of canvas expand top
        if self.loc[1] == (canvas_shape[1] - 2):
            a = np.zeros((canvas_shape[0], 10, 2), dtype=bool)
            self.canvas = np.concatenate((self.canvas, a), axis=1)

        # if loc at left of canvas expand left
        elif self.loc[0] == 1:
            a = np.zeros((10, canvas_shape[1], 2), dtype=bool)
            self.canvas = np.concatenate((a, self.canvas), axis=0)
            self.loc[0] += 10 #adjust loc to reflect change

        # if loc at bottom of canvas expand down
        elif self.loc[1] == 1:
            a = np.zeros((canvas_shape[0], 10, 2), dtype=bool)
            self.canvas = np.concatenate((a, self.canvas), axis=1)
            self.loc[1] +=10 # adjust loc to reflect change

        # if loc at right of canvas, expand right
        elif self.loc[0] == (canvas_shape[0] - 2):
            a = np.zeros((10, canvas_shape[1], 2), dtype=bool)
            self.canvas = np.concatenate((self.canvas, a), axis=0)

        
    def paint(self, color: bool):
        "marks the color and flags the visit to the location"
        # set the color
        self.canvas[self.loc[0], self.loc[1], 0] = color

        # flag has visited
        self.canvas[self.loc[0], self.loc[1], 1] = True

    def get_current_color(self):
        "returns the current color"
        return self.canvas[self.loc[0], self.loc[1], 0]
        
        
def display_pixels(arr):
    image = arr.reshape((arr.shape[0], arr.shape[1]))
    plt.matshow(image)
    plt.show()
    

def main():
    # read input
    puzzle_input = get_input('input.txt')

    # create hull painter
    painter = Painter()

    # create intcode computer
    comp = IntcodeComp(puzzle_input)

    # run the computer and painter
    while True:
        # input the current color to get color, turn, stop
        color, turn, stop = comp.compute(input_signal=painter.get_current_color())
        # if computer is stopped, stop
        if stop:
            break
        # otherwise paint and move based on computer's directions
        painter.paint(color)
        painter.move(turn)

    # print the number of panels painted at least once
    display_pixels(painter.canvas[:,:,0])


if __name__ == "__main__":
    main()