import sys
sys.path.append('/Users/allisonhonold/ds0805/advent_of_code')

from day_5.day5_pt2 import get_input
from itertools import permutations

def get_permutations(min, max):
    """creates a list of tuples, each a permutation of the numbers between 
    min and max inclusive.
    """
    nums = list(range(min, max+1))
    return list(permutations(nums))


def calculate_output(phase_setting_list, intcode_input):
    """Calculates the output when the intocode is run four times with the 
    settings given by phase_setting_list and the input starting with 0, and
    then each output providing the input value for the next stage.
    """
    input_signal = 0
    for i in range(len(phase_setting_list)):
        input_signal = intcode_comp(intcode_input, phase_setting_list[i], 
                                    input_signal)
    return input_signal


def main():
    # read input
    puzzle_input = get_input('day7_input.txt')

    # determine combinations of phase settings
    phase_settings = get_permutations(0,4)

    # test each set of phase settings, collecting output numbers
    outputs = []
    for phase_setting in phase_settings:
        output = calculate_output(phase_setting, puzzle_input)
        outputs.append(output)

    # print max output number
    print(max(outputs))


def t(puzzle_input):
    """main for testing purposes"""
    # determine combinations of phase settings
    phase_settings = get_permutations(0,4)

    # test each set of phase settings, collecting output numbers
    outputs = []
    for phase_setting in phase_settings:
        output = calculate_output(phase_setting, puzzle_input)
        outputs.append(output)

    # print max output number
    return(max(outputs))


def intcode_comp(puzzle_input, phase_setting, input_signal):
    """Compute based on the intcode instructions below
    # position mode:
        # 1: positional add
        # 2: positional multiply
        # 3: get input and save it at location of parameter
        # 4: output value located at parameter

    # immediate mode:
        # same as above but use the parameters as values not locations

    # 99: stop

    instruction
        opcode: rightmost 2 digits
        parameter mode: one per parameter read right to left
    """
    # mark current location in puzzle input
    current = 0

    # mark whether input is on step 0 (phase setting) or 1 (input sig)
    step = 0

    while (True):
        prev_current = current
        prev_instruction = puzzle_input[prev_current]
        opcode, modes, current = parse_instruction(puzzle_input, current)
        if opcode == '99':
            break
        params, current = get_parameters(current, puzzle_input, opcode)
        values = get_values(modes, params, puzzle_input)
        if opcode == '01':
            puzzle_input = add(values, puzzle_input)
        elif opcode == '02':
            puzzle_input = multiply(values, puzzle_input)
        elif opcode =='03':
            if step == 0:
                u_input = phase_setting
            elif step == 1:
                u_input = input_signal
            puzzle_input = process_input(values, puzzle_input, u_input)
            step += 1
        elif opcode == '04':
            output = get_output(values, puzzle_input)
        elif opcode == '05':
            current = jump_if_true(params, modes, values, current, puzzle_input)
        elif opcode == '06':
            current = jump_if_false(params, modes, values, current, puzzle_input)
        elif opcode == '07':
            puzzle_input = less_than(values, puzzle_input)
        elif opcode == '08':
            puzzle_input = equals(values, puzzle_input)
        if prev_instruction != puzzle_input[prev_current]:
            current = prev_current
    return output


def equals(values, puzzle_input):
    """if the first parameter is equal to the second parameter, it stores 1 in
    the position given by the third parameter. Otherwise, it stores 0.
    """
    if values[0] == values[1]:
        puzzle_input[values[2]] = 1
    else:
        puzzle_input[values[2]] = 0
    return puzzle_input


def less_than(values, puzzle_input):
    """if the first parameter is less than the second parameter, it stores 1 in
    the position given by the thrid parameter. Otherwise it stores 0.
    """
    if values[0] < values[1]:
        puzzle_input[values[2]] = 1
    else:
        puzzle_input[values[2]] = 0
    return puzzle_input


def jump_if_false(params, modes, values, current, puzzle_input):
    """If the first parameter is non-zero, it sets the instruction pointer to 
    the value from the second parameter. Otherwise, it does nothing.
    """
    if values[0] == 0:
        # print(f"modes[1]: {modes[1]}")
        if modes[1] == 0:
            # print(f"puzzle_input[params[1]]: {puzzle_input[params[1]]}")
            current = puzzle_input[params[1]]
            # print(f"current: {current}")
            # print(f"puzzle_input[current]: {current}")
        elif modes[1] == 1:
            # print(f"params[1]: {params[1]}")
            current = params[1]
    return current


def jump_if_true(params, modes, values, current, puzzle_input):
    """If the first parameter is non-zero, it sets the instruction pointer to 
    the value from the second parameter. Otherwise, it does nothing.
    """
    if values[0] != 0:
        # print(f"modes[1]: {modes[1]}")
        if modes[1] == 0:
            # print(f"puzzle_input[params[1]: {puzzle_input[params[1]]}")
            current = puzzle_input[params[1]]
        elif modes[1] == 1:
            # print(f"params[1]: {params[1]}")
            current = params[1]
    return current


def add(values, puzzle_input):
    """Adds the first two values and records them at the location of the third
    "value" in the puzzle input. Then returns the resulting puzzle input.
    """
    result = values[0] + values[1]
    puzzle_input[values[2]] = result
    return puzzle_input


def multiply(values, puzzle_input):
    """Multiplies the first two values and records them at the location of the third
    "value" in the puzzle input. Then returns the resulting puzzle input.
    """    
    result = values[0] * values[1]
    puzzle_input[values[2]] = result
    return puzzle_input   


def process_input(values, puzzle_input, u_input):
    """Takes input from the user and records them in the location specified
    by the "value", and returns the resulting puzzle input
    """
    puzzle_input[values[0]] = u_input
    return puzzle_input


def get_output(values, puzzle_input):
    """returns the value for output
    """
    return puzzle_input[values[0]]


def parse_instruction(puzzle_input, current):
    """parses the instructions stored in the current position of the input
    """
    instruction = str(puzzle_input[current]).zfill(5)
    opcode = instruction[-2:]
    modes = [int(instruction[2]), int(instruction[1]), int(instruction[0])]
    current += 1
    return opcode, modes, current


def get_parameters(current, puzzle_input, opcode):
    """extracts the parameters from the input and updates the current location
    """
    if opcode == '03' or opcode == '04':
        params = [puzzle_input[current]]
        current += 1
    elif opcode == '05' or opcode == '06':
        params = [puzzle_input[current], 
                  puzzle_input[current+1]]
        current += 2      
    else:
        params = [puzzle_input[current], 
                  puzzle_input[current+1], 
                  puzzle_input[current+2]]
        current += 3
    return params, current


def get_values(modes, params, puzzle_input):
    """Gets the values from the puzzle input using the provided modes and 
    parameters.
    """
    params_cp = params.copy()
    loc = params_cp.pop(-1)
    values = []
    for i, param in enumerate(params_cp):
        if modes[i] == 0: #position mode
            values.append(puzzle_input[param])
        if modes[i] == 1: #immediate mode
            values.append(param)
    values.append(loc)
    return values


if __name__ == "__main__":
    main()