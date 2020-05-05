import re

def read_input(filename):
    'reads the text file'
    text_file = open(filename, "r")
    input_str = text_file.readlines()
    text_file.close()
    return input_str


def extract_positions(lines):
    """extracts postiions from a list of lines with each line representing a 
    moon eg. <x=-1, y=-4, z=0>

    Returns positions as a list of lists, with each list representing a moon
    with indices 0,1,2 representing x,y,z for each moon.
    """
    positions = []
    for line in lines:
        position = [int(s) for s in re.findall(r'-?\d+', line)]
        positions.append(position)
    return positions


def apply_gravity(pos, vels):
    """applies gravity by comparing each moon to each other and incrementing
    or decrementing velocity by one based on relative position in each 
    dimension
    """
    vels = compare(0, 1, pos, vels)
    vels = compare(0, 2, pos, vels)
    vels = compare(0, 3, pos, vels)
    vels = compare(1, 2, pos, vels)
    vels = compare(1, 3, pos, vels)
    vels = compare(2, 3, pos, vels)
    return vels


def compare(first, second, pos, vels):
    for i in range(3):
        if pos[first][i] < pos[second][i]:
            vels[first][i] += 1
            vels[second][i] += -1
        elif pos[first][i] > pos[second][i]:
            vels[first][i] += -1
            vels[second][i] += 1
    return vels


def apply_velocities(pos, vels):
    """applies velocities by adding velocity to the position for each moon in 
    each dimension
    """
    for i, moon_position in enumerate(pos):
        for dimmension, _ in enumerate(moon_position):
            moon_position[dimmension] += vels[i][dimmension]
    return pos


def calc_energy(pos, vels):
    """calculates the sum of the total energies of the moons. Each moon's 
    potential energy is the sum of the absolute values of its position 
    components. Its kinetic energy is the sum of the absolute values of its 
    velocity components. The total energy for a moon is the product of the 
    kinetic and potential energies.
    """
    total_energy = 0
    for i in range(len(pos)):
        abs_positions = [abs(x) for x in pos[i]]
        abs_vels = [abs(x) for x in vels[i]]
        total_energy += sum(abs_positions) * sum(abs_vels)
    return total_energy

def main():
    # read input positions
    lines = read_input('input.txt')
    pos = extract_positions(lines)

    # set starting velocities
    vels = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # step through 1000 time steps
    for _ in range(1000):
        vels  = apply_gravity(pos, vels)
        pos = apply_velocities(pos, vels)

    # calculate and print total energy
    print(calc_energy(pos, vels))

if __name__ == "__main__":
    main()