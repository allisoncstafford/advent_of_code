import re
import math
from d14 import calc_cost

def read_input(filename):
    'reads the text file'
    text_file = open(filename, "r")
    input_str = text_file.readlines()
    text_file.close()
    return input_str


def parse_rxns(input_text):
    elements = {}
    for line in input_text:
        nums = [int(s) for s in re.findall(r'\d+', line)]
        chems = [s for s in re.findall(r'[A-Z]+', line)]
        chem_sets = [[n, c] for n,c in zip(nums, chems)]
        inputs = chem_sets[0:-1]
        output = chem_sets[-1]
        elements[output[1]] = {'n_out': output[0], 'inputs': inputs}
    return elements

def search(elements, high, low, target):
    while low <= high:
        mid = math.floor((low + high)/2)
        cost_mid = calc_cost(elements, amount=mid)
        if cost_mid < target:
            low = mid+1
        elif cost_mid > target:
            high = mid-1
        else:
            return mid
    
    print('returning low -1')
    return low -1


def main():
    # read inupt
    input_text = read_input("input.txt")

    # set ore_per_fuel
    ore_per_fuel = 319014

    # parse input into reactions
    elements = parse_rxns(input_text)

    # get leftovers after making as many single fuel batches as possible
    ore_input = 1000000000000

    min_fuel = math.floor(ore_input/ore_per_fuel)
    max_fuel = min_fuel * 2
    
    print(search(elements, max_fuel, min_fuel, ore_input))


 



if __name__ == "__main__":
    main()