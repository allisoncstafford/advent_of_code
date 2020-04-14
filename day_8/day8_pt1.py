from itertools import zip_longest


def get_layers(data, width, height):
    """transforms data string into a list of lists

    Args:
        data: string of data
        width: desired layer width
        height: desired layer height
    
    returns: a list of tuples, each representing a layer of pixels
    """
    data = [int(char) for char in data]
    layer_size = width * height
    layers = grouper(data, layer_size)
    return layers


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks.
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    Source: adapted from itertools recipes

    Returns: a list of tuples of length n
    """
    args = [iter(iterable)] * n
    return list(zip_longest(*args, fillvalue=fillvalue))


def read_single_data(filename):
    """reads the input from a single line file and returns the string

    Args: file: filename/path
    Returns: str
    """
    text_file = open(filename, "r")
    input_str = text_file.readlines()
    text_file.close()
    return input_str[0]


def get_counts(layers):
    """gets the count of digits for each layer in layers

    Args: layers - a list of tuples
    Returns: list of dictionaries of the count of digits 0-9
    """
    dicts = [layer_counts(layer) for layer in layers]
    return dicts


def layer_counts(layer):
    """counts the digits in a layer

    args: layer (a tuple of digits 0-9)
    returns: dictionary with keys 0-9, values are the frequency of the key
    """
    counts = {i:layer.count(i) for i in range(10)}
    return counts


def get_fewest(list_of_counts, num):
    """returns the layer with the fewest of the number
    """
    number_seq = [d[num] for d in list_of_counts]
    loc = number_seq.index(min(number_seq))
    return list_of_counts[loc]


def main():
    # read data from day8_input.txt
    data = read_single_data('day8_input.txt')

    # divide input into layers of size 25 x 6
    layers = get_layers(data, 25, 6)

    # get digit counts for each layer
    counts = get_counts(layers)

    # from the layer with fewest 0s, print the # of 1s * # of 2s
    few_0s = get_fewest(counts, 0)
    ones = few_0s[1]
    twos = few_0s[2]
    print(ones*twos)

def t(data, width, height):
    """function for testing main"""
    # divide input into layers of size 25 x 6
    layers = get_layers(data, width, height)

    # get digit counts for each layer
    counts = get_counts(layers)

    # from the layer with fewest 0s, print the # of 1s * # of 2s
    few_0s = get_fewest(counts, 0)
    ones = few_0s[1]
    twos = few_0s[2]
    return(ones*twos)

if __name__ == "__main__":
    main()