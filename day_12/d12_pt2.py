from d12 import read_input
import re

def extract_positions(lines):
    """extracts postiions from a list of lines with each line representing a 
    moon eg. <x=-1, y=-4, z=0>

    Returns positions as a list, with each set of 3 representing a moon
    with x,y,z position.
    """
    positions = []
    for line in lines:
        for s in re.findall(r'-?\d+', line):
            positions.append(int(s))
    return positions


def apply_gravity(pos_vels):
    """applies gravity by comparing each moon to each other and incrementing
    or decrementing velocity by one based on relative position in each 
    dimension
    """
    pos_vels = compare(0, 1, pos_vels)
    pos_vels = compare(0, 2, pos_vels)
    pos_vels = compare(0, 3, pos_vels)
    pos_vels = compare(1, 2, pos_vels)
    pos_vels = compare(1, 3, pos_vels)
    pos_vels = compare(2, 3, pos_vels)
    return pos_vels


def compare(first, second, pos_vels):
    vel1 = first + 4
    vel2 = second + 4
    # if position 1 is less than position 2, position 1 inc 2 dec
    if pos_vels[first] < pos_vels[second]:
        pos_vels[vel1] += 1
        pos_vels[vel2] += -1
    # if position 1 is greater than position 2, position 1 dec 1 inc
    elif pos_vels[first] > pos_vels[second]:
        pos_vels[vel1] += -1
        pos_vels[vel2] += 1
    return pos_vels


def apply_velocities(pos_vels):
    """applies velocities by adding velocity to the position for each moon in 
    each dimension
    """
    for i in range(4):
        pos_vels[i] += pos_vels[i + 4]
    return pos_vels


def parse_dimensions(pos_vels):
    "separate the x, y, and z components from input list"
    x0s = []
    y0s = []
    z0s = []

    for i, n in enumerate(pos_vels):
        if i % 3 == 0:
            x0s.append(n)
        if i % 3 == 1:
            y0s.append(n)
        if i % 3 == 2:
            z0s.append(n)
    
    return x0s, y0s, z0s


def calc_cycle(pos_vels0):
    "calculates the cycle time for a single dimension"
    count = 0
    pos_vels = pos_vels0.copy()

    while True:
        pos_vels = apply_gravity(pos_vels)
        pos_vels = apply_velocities(pos_vels)
        count += 1
        if pos_vels == pos_vels0:
            break
    
    return count


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def main():
    # read input positions
    lines = read_input('input.txt')
    pos_vels = extract_positions(lines)

    # add starting velocities to positions
    pos_vels.extend([0]*12)

    x0s, y0s, z0s = parse_dimensions(pos_vels)

    # count cycle times
    x_cycle = calc_cycle(x0s)
    y_cycle = calc_cycle(y0s)
    z_cycle = calc_cycle(z0s)

    # find lowest common denomenator btwen x, y, z
    print(lcm(x_cycle, lcm(y_cycle, z_cycle)))



if __name__ == "__main__":
    main()