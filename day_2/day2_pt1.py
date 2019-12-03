# Day 2: 1202 Program Alarm

def intcode(input):
    """simulates an intcode computer with opcodes 1, 2, and 99. 1 adds the
    numbers at locations specified by the following two parameters. 2 
    multiplies the numbers at locations specified by the following two
    parameters. 99 stops the funtion.

    Args:
        input: a list of ints with encoded instructions (see above)
    
    Returns:
        a copy of the list with the instructions carried out.
    """
    # initialize processed list
    p_list = input.copy()

    # initialize location of opcode, n1, n2, and result
    o_pos = 0
    n1_pos = 1
    n2_pos = 2
    r_pos = 3

    while(True):
        # complete the calculation, placing the result in the result position
        if p_list[o_pos] == 1:
            p_list[p_list[r_pos]] = (p_list[p_list[n1_pos]] 
                                         + p_list[p_list[n2_pos]])
        elif p_list[o_pos] == 2:
            p_list[p_list[r_pos]] = (p_list[p_list[n1_pos]] 
                                        * p_list[p_list[n2_pos]])
        elif p_list[o_pos] == 99:
            return p_list

        # increment to the next set of locations
        o_pos += 4
        n1_pos += 4
        n2_pos += 4
        r_pos += 4


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
    """Reads the input, resets the 2nd and 3rd int to recreate the problem
    described in the challenge, and prints the result.
    """
    input = get_input('day2_input.txt')
    input[1] = 12
    input[2] = 2
    output = intcode(input)
    print(output[0])


if __name__ == "__main__":
    main()
    
