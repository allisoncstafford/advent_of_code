from day8_pt1 import read_single_data, get_layers
from matplotlib import pyplot as plt
import numpy as np

def get_prominent_color(layers):
    """returns the first non-transparent pixel color for each pixel"""
    final = [3] * len(layers[0])
    for i in range(len(final)):
        for layer in layers:
            if layer[i] != 2:
                final[i] = layer[i]
                break
    return final


def display_pixels(layer, n_rows, n_cols):
    image = np.array(layer)
    image = image.reshape((n_rows, n_cols))
    plt.matshow(image)
    plt.show()

def main():
    # read input
    data = read_single_data('day8_input.txt')

    # get the layers
    layers = get_layers(data, 25, 6)

    # get prominent color
    pixels = get_prominent_color(layers)

    # display pixels (0=black, 1=white)
    display_pixels(pixels, 6, 25)


if __name__ == "__main__":
    main()