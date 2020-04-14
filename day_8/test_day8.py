from day8_pt1 import get_layers, layer_counts, t
from day8_pt2 import display_pixels, get_prominent_color

def test_get_layers():
    inputs = '123456789012'
    assert get_layers(inputs, 3, 2) == [(1,2,3,4,5,6), (7,8,9,0,1,2)]

def test_layer_counts():
    layer = [0,1,2,3,4,5]
    assert layer_counts(layer) == {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:0, 7:0, 8:0, 9:0}

def test_main():
    inputs = '122456789012'
    assert t(inputs, 3, 2) == 2

def test_display():
    inputs = [0,1,2,3,4,5]
    assert display_pixels(inputs, 2, 3) == None

def test_get_prominent_color():
    inputs = [(0,2,2,2), (1,1,2,2), (2,2,1,2), (0,0,0,0)]
    assert get_prominent_color(inputs) == [0, 1, 1, 0]

def test_display2():
    inputs = [(0,2,2,2), (1,1,2,2), (2,2,1,2), (0,0,0,0)]
    pixels = get_prominent_color(inputs)
    assert display_pixels(pixels, 2, 2) == None
