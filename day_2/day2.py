# Day 2: 1202 Program Alarm

# load necessary packages

def intcode(input):
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