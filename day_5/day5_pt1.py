import numpy as np

def intcode_comp(puzzle_input):
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
    current = 0

    while (True):
        opcode, modes, current = parse_instruction(puzzle_input, current)
        # print(f'opcode: {opcode}, modes: {modes}, current: {current}')
        if opcode == '99':
            break
        params, current = get_parameters(current, puzzle_input, opcode)
        # print(f'params: {params}, current: {current}')
        values = get_values(modes, params, puzzle_input)
        # print(f'values: {values}')
        if opcode == '01':
            puzzle_input = add(values, puzzle_input)
        elif opcode == '02':
            puzzle_input = multiply(values, puzzle_input)
        elif opcode =='03':
            puzzle_input = get_user_input(values, puzzle_input)
        elif opcode == '04':
            output(values, puzzle_input)
        # print(puzzle_input)


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


def get_user_input(values, puzzle_input):
    """Takes input from the user and records them in the location specified
    by the "value", and returns the resulting puzzle input
    """
    user_input = int(input('enter the value: '))
    puzzle_input[values[0]] = user_input
    return puzzle_input


def output(values, puzzle_input):
    """outputs the "value", and returns the resulting puzzle input
    """
    print(f'output value: {puzzle_input[values[0]]}')


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
    loc = params.pop(-1)
    values = []
    for i, param in enumerate(params):
        if modes[i] == 0: #position mode
            values.append(puzzle_input[param])
        if modes[i] == 1: #immediate mode
            values.append(param)
    values.append(loc)
    return values



def get_input(filename):
    """returns list of inputs from data file. File should have integer values, 
    separated by commas

    Args:
        filename: the name of the file with the input data.

    Returns:
        a list of integers read from the file
    """
    text_file = open(filename, "r")
    input_str = text_file.readlines()
    text_file.close()
    input_list = input_str[0].split(',')
    input_ints = list(map(int, input_list))
    return input_ints


def main():
    puzzle_input = get_input('day5_input.txt')
    intcode_comp(puzzle_input)


if __name__ == "__main__":
    main()