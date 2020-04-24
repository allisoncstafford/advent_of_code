from operator import attrgetter
from day10_pt1 import read_lines, get_best
import numpy as np
import math

class Astroid():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n_detects = None
        self.angle_to_laser = None
        self.dist_to_laser = None

    def set_n_detects(self, astroids):
        count = 0
        blocked_slopes_right = []
        blocked_slopes_left = [] # accounting for  -/- ==> pos
        for astroid in astroids:
            # initialize bool right
            right = False

            if astroid != self:
                # check for divide by zero error
                if astroid.x - self.x == 0:
                    if astroid.y - self.y > 0:
                        slope = 'below'
                    if astroid.y - self.y < 0:
                        slope = 'above'
                else:
                    # calculate slope
                    slope = (astroid.y - self.y)/(astroid.x - self.x)

                    # check for right/left
                    if astroid.x - self.x >= 0:
                        right = True

                # if not blocked/duplicated, add slope to list of slopes and count
                if (right) and (slope not in blocked_slopes_right):
                    count += 1
                    blocked_slopes_right.append(slope)

                elif (not right) and (slope not in blocked_slopes_left):
                    count += 1
                    blocked_slopes_left.append(slope)
        self.n_detects = count


    def set_angle(self, angle):
        self.angle_to_laser = angle

    
    def set_distance(self, dist):
        self.dist_to_laser = dist


def set_laser(laser, astroids):
    """for the given astroid set, determines angle and distance to laser for
    each astroid besides the laser astroid
    """
    for astroid in astroids:
        if astroid != laser:
            # reset origin to laser
            x = astroid.x - laser.x
            y = laser.y - astroid.y

            # determine angle between <0,1> and laser-to-astroid vector
            v1 = (0, 1)
            v2 = (x, y)
            smallest_angle = angle_between(v1, v2)
            if x < 0:
                angle = 2*math.pi - smallest_angle
            else:
                angle = smallest_angle
            astroid.set_angle(round(angle, 4))

            # determine the distance between laser and astroid
            astroid.set_distance(math.sqrt(x**2 + y**2))
            

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def sort_astroids(laser, astroids):
    astrs = [a for a in astroids if a != laser]

    # organize astroids by angle
    angles = list(sorted(set([a.angle_to_laser for a in astrs])))
    angle_dist_dict = {angle:[] for angle in angles}

    for a in astrs:
        angle_dist_dict[a.angle_to_laser].append((a.dist_to_laser, a))
    
    for key in angle_dist_dict.keys():
        angle_dist_dict[key] = sorted(angle_dist_dict[key], key=lambda x: x[0])

    # moving through increasing angles, add astroid with shortest distance
    sorted_astrs = []
    count = 0

    while count < len(astrs):
        for angle in angles:
            if len(angle_dist_dict[angle]) > 0:
                len_astroid_tup = angle_dist_dict[angle].pop(0)
                sorted_astrs.append(len_astroid_tup[1])
                count += 1

    return sorted_astrs


def create_astroids(input_lines):
    """creates a list of Astroids from .#...# inputs"""
    astroids = []
    for y, line in enumerate(input_lines):
        for x, char in enumerate(line):
            if char == '#':
                astroids.append(Astroid(x, y))
    return astroids


def main():
    # read input
    input_lines = read_lines('day10_input.txt')

    # parse into (x,y) positions
    astroids = create_astroids(input_lines)

    # get number each can detect
    for astroid in astroids:
        astroid.set_n_detects(astroids)

    # get best (max num able to detect)
    best_astroids = get_best(astroids)
    laser = best_astroids[0]

    # set the laser to the best location, getting angles and distances
    set_laser(laser, astroids)

    # sort astroids by angle and distance
    sorted_astroids = sort_astroids(laser, astroids)

    print(f"200th astroid: ({sorted_astroids[199].x},{sorted_astroids[199].y})")



if __name__ == "__main__":
    main()