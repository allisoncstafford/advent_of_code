# see challenge instructions: https://adventofcode.com/2019/day/1#part2

# import necessary packages
import math
from day1_pt1 import get_input

def fuel_counter_inc_fuel(module_masses):
    """counts the amount of fuel needed (take each mass, divide by three, round 
    down, and subtract 2. Then sum all the values). Considers the fuel needed
    to transport the added fuel weight

    Args:
        module_masses: an iterable of module masses
    Returns:
        fuel: total fuel needed based on the module masses and the fuel weights
    """
    # counter
    fuel = 0

    # iterate through modules
    for module_mass in module_masses:
        last_fuel = calc_fuel(module_mass)
        while last_fuel > 0:
            fuel += last_fuel
            last_fuel = calc_fuel(last_fuel)

    # return total fuel needed
    return fuel


def calc_fuel(mass):
    """Calculates the fuel needed to transport a mass (take each mass, divide by 
    three, round down, and subtract 2) without regard to the added mass of the
    fuel.

    Args:
        mass: mass

    Returns:
        fuel needed (int)
    """
    return math.floor(mass/3) - 2


if __name__ == "__main__":
    input = get_input("day1_input.txt")
    print(fuel_counter_inc_fuel(input))