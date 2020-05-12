from scipy.sparse import dok_matrix

class IntcodeComp():
    def __init__(self, intcode):
        # intcode converted to sparse array for giant size
        size = max([len(intcode)+1, max(intcode)+1])
        self.code = dok_matrix((1, size), dtype=int)
        for i in range(len(intcode)):
            self.code[0,i] = intcode[i]
        self.current = 0
        self.stopped = False
        # self.input_code1 = input_code1
        # self.phase_setting = phase
        # self.input_step = 0
        # self.name = name
        self.relative_base = 0

    def stop(self):
        self.stopped = True

    def compute(self, input_signal=None):
        """Compute based on the intcode instructions below
        # position mode:
            # 1: positional add
            # 2: positional multiply
            # 3: get input and save it at location of parameter
            # 4: output value located at parameter

        # immediate mode:
            # same as above but use the parameters as values not locations

        # 99: stops

        instruction
            opcode: rightmost 2 digits
            parameter mode: one per parameter read right to left
        """
        outputs = []
        while (True):
            prev_current = self.current
            prev_instruction = self.code[0, prev_current]
            opcode, modes, self.current = parse_instruction(self.code, self.current)
            if opcode == '99':
                self.stop()
                return outputs
            params, self.current = get_parameters(self.current, self.code, opcode)
            values, target_loc = get_values(modes, params, self.code, 
                                            self.current, self.relative_base)
            if opcode == '01':
                self.code = add(values, target_loc, self.code)
            elif opcode == '02':
                self.code = multiply(values, target_loc, self.code)
            elif opcode =='03':
                if outputs != []:
                    self.current = prev_current
                    return outputs
                else:
                    u_input = input_signal
                    self.code = process_input(self.code, u_input, target_loc)
            elif opcode == '04':
                outputs.append(get_output(self.code, target_loc))
            elif opcode == '05':
                self.current = jump_if_true(params, modes, values, target_loc,
                                            self.current, self.code)
            elif opcode == '06':
                self.current = jump_if_false(params, modes, values, target_loc,
                                             self.current, self.code)
            elif opcode == '07':
                self.code = less_than(values, target_loc, self.code)
            elif opcode == '08':
                self.code = equals(values, target_loc, self.code)
            elif opcode =='09':
                self.relative_base += self.code[0, target_loc]
            
            # check if the instruction has been altered
            instruction_value = self.code[0, prev_current]
            if prev_instruction != instruction_value:
                self.current = prev_current

def equals(values, target_loc, puzzle_input):
    """if the first parameter is equal to the second parameter, it stores 1 in
    the target location. Otherwise, it stores 0.
    """
    if values[0] == values[1]:
        puzzle_input[0, target_loc] = 1
    else:
        puzzle_input[0, target_loc] = 0
    return puzzle_input


def less_than(values, target_loc, puzzle_input):
    """if the first parameter is less than the second parameter, it stores 1 in
    the target location. Otherwise it stores 0.
    """
    if values[0] < values[1]:
        puzzle_input[0, target_loc] = 1
    else:
        puzzle_input[0, target_loc] = 0
    return puzzle_input


def jump_if_false(params, modes, values, target_loc, current, puzzle_input):
    """If the first parameter is zero, it sets the instruction pointer to 
    the target location. Otherwise, it does nothing.
    """
    if values[0] == 0:
        # if modes[1] == 0:
        #     current = puzzle_input[params[1]]
        # elif modes[1] == 1:
        #     current = params[1]
        current = puzzle_input[0, target_loc]
    return current


def jump_if_true(params, modes, values, target_loc, current, puzzle_input):
    """If the first parameter is non-zero, it sets the instruction pointer to 
    the second value. Otherwise, it does nothing.
    """
    if values[0] != 0:
        # if modes[1] == 0:
        #     current = puzzle_input[params[1]]
        # elif modes[1] == 1:
        #     current = params[1]
        # elif modes[1] == 2:
        #     current = puzzle_input[params[1] + relative base]
        current = puzzle_input[0, target_loc]
    return current


def add(values, target_loc, puzzle_input):
    """Adds the first two values and records them at the target location in the
    puzzle input. Then returns the resulting puzzle input.
    """
    result = values[0] + values[1]
    puzzle_input[0, target_loc] = result
    return puzzle_input


def multiply(values, target_loc, puzzle_input):
    """Multiplies the first two values and records them at the target location
    in the puzzle input. Then returns the resulting puzzle input.
    """    
    result = values[0] * values[1]
    puzzle_input[0, target_loc] = result
    return puzzle_input   


def process_input(puzzle_input, u_input, target_loc):
    """Records the passed u_input in the location specified, and returns the 
    resulting puzzle input
    """
    puzzle_input[0, target_loc] = u_input
    return puzzle_input


def get_output(puzzle_input, target_loc):
    """returns the value for output
    """
    return puzzle_input[0, target_loc]


def parse_instruction(puzzle_input, current):
    """parses the instructions stored in the current position of the input
    """
    instruction = str(puzzle_input[0, current]).zfill(5)
    opcode = instruction[-2:]
    modes = [int(instruction[2]), int(instruction[1]), int(instruction[0])]
    current += 1
    # print(f"modes: {modes}")
    return opcode, modes, current


def get_parameters(current, puzzle_input, opcode):
    """extracts the parameters from the input and updates the current location
    """
    if opcode in ['03', '04', '09']:
        params = [puzzle_input[0, current]]
        current += 1
    elif opcode == '05' or opcode == '06':
        params = [puzzle_input[0, current], 
                  puzzle_input[0, current+1]]
        current += 2      
    else:
        params = [puzzle_input[0, current], 
                  puzzle_input[0, current+1], 
                  puzzle_input[0, current+2]]
        current += 3
    return params, current


def get_values(modes, params, puzzle_input, current, relative_base=None):
    """Gets the values and the target location from the puzzle input using the
    provided modes and parameters.
    """
    params_rev = list(reversed(params))
    values_rev = []
    modes_rev = list(reversed(modes[:len(params_rev)]))
    target_loc = None
    for i, param in enumerate(params_rev):
        if i == 0: # target location
            if modes_rev[i] == 0:
                target_loc = param
            elif modes_rev[i] == 2:
                target_loc = param + relative_base
            elif modes_rev[i] == 1:
                target_loc = current - 1
        else:
            if modes_rev[i] == 0: #position mode
                values_rev.append(puzzle_input[0, param])
            if modes_rev[i] == 1: #immediate mode
                values_rev.append(param)
            if modes_rev[i] == 2: # relative mode
                values_rev.append(puzzle_input[0, param + relative_base])
    values = list(reversed(values_rev))
    return values, target_loc