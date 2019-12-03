# see challenge instructions: https://adventofcode.com/2019/day/1

# import necessary packages
import math

def fuel_counter(module_masses):
    """counts the amount of fuel needed (take each mass, divide by three, round 
    down, and subtract 2. Then sum all the values).

    Args:
        module_masses: an iterable of module masses
    Returns:
        fuel: total fuel needed based on the module masses
    """
    # counter
    fuel = 0

    # iterate through modules
    for module_mass in module_masses:
        fuel += math.floor(module_mass/3) - 2

    # return total fuel needed
    return fuel


def get_input(filename):
    """returns list of inputs from data file. File should have integer values, 
    one per line.

    Args:
        filename: the name of the file with the input data.

    Returns:
        a list of integers read from the file
    """
    text_file = open(filename, "r")
    input_strs = text_file.readlines()
    text_file.close()
    input_ints = list(map(int, input_strs))
    return input_ints


if __name__ == "__main__":
    input = get_input("day1_input.txt")
    print(fuel_counter(input))