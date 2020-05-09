import re
import math

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

def calc_cost(elements, element='FUEL', amount=1, inventory={}):
    if element == "ORE":
        return amount

    # check inventory and adjust
    if element in inventory.keys():
        inventory_amt = inventory[element]
    else:
        inventory_amt = 0
    amt_needed = amount - inventory_amt
    if amt_needed < 0:
        inventory[element] = -1 * amt_needed
        amt_needed = 0
    else:
        inventory[element] = 0

    # use the recipe
    need = 0
    if amt_needed > 0:
        recipe = elements[element]
        n_out = recipe["n_out"]
        inputs = recipe["inputs"]
        multiplier = math.ceil(amt_needed / n_out)
        production = [(n*multiplier, elem) for n, elem in inputs]
        if amt_needed < n_out * multiplier:
            inventory[element] = n_out * multiplier - amt_needed
        for n, e in production:
            need += calc_cost(elements, element=e, amount=n, inventory=inventory)

    return need


def main():
    # read inupt
    input_text = read_input("input.txt")

    # parse input into reactions
    elements = parse_rxns(input_text)

    # from fuel, work backward counting inputs
    print(calc_cost(elements))


if __name__ == "__main__":
    main()