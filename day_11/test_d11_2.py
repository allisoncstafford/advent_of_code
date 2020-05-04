from day11_pt2 import Painter

def test_move_left():
    painter = Painter()
    painter.move(0)
    assert painter.loc == [4,5]
    assert painter.direction == 'left'

def test_move_right():
    painter = Painter()
    painter.move(1)
    assert painter.loc == [6,5]
    assert painter.direction == 'right'

def test_move_up():
    painter = Painter()
    painter.move(1)
    painter.move(0)
    assert painter.loc == [6,6]
    assert painter.direction == 'up'

def test_move_down():
    painter = Painter()
    painter.move(1)
    painter.move(1)
    assert painter.loc == [6,4]
    assert painter.direction == 'down'

def test_expand_grid_right():
    painter = Painter()
    for _ in range(3):
        painter.move(1)
        painter.move(1)
        painter.move(0)
        painter.move(0)
    assert painter.loc == [11,5]
    assert painter.canvas.shape == (20,10,2)

def test_expand_grid_left():
    painter = Painter()
    for _ in range(3):
        painter.move(0)
        painter.move(0)
        painter.move(1)
        painter.move(1)
    assert painter.loc == [9,5]
    assert painter.canvas.shape == (20,10,2)

def test_expand_grid_up():
    painter = Painter()
    for _ in range(3):
        painter.move(1)
        painter.move(0)
        painter.move(0)
        painter.move(1)
    assert painter.loc == [5, 11]
    assert painter.canvas.shape == (10,20,2)

def test_expand_grid_down():
    painter = Painter()
    painter.move(0)
    painter.move(0)
    painter.move(0)
    painter.move(1)
    for _ in range(2):
        painter.move(1)
        painter.move(0)
        painter.move(0)
        painter.move(1)
    assert painter.loc == [5, 9]
    assert painter.canvas.shape == (10,20,2)

def test_paint():
    painter = Painter()
    painter.paint(1)
    assert painter.canvas[5,5,0] == 1
    assert painter.canvas[5,5,1] == 1

def test_paint2():
    painter = Painter()
    for _ in range(4):
        painter.paint(0)
        painter.move(1)
    assert painter.canvas[5,5,0] == 0
    assert painter.canvas[5,5,1] == 1
    assert painter.canvas[6,5,0] == 0
    assert painter.canvas[6,5,1] == 1
    assert painter.canvas[6,4,0] == 0
    assert painter.canvas[6,4,1] == 1
    assert painter.canvas[5,4,0] == 0
    assert painter.canvas[5,4,1] == 1

def test_get_count():
    painter = Painter()
    for _ in range(4):
        painter.paint(0)
        painter.move(1)
    assert painter.get_count() == 4

def test_get_count2():
    painter = Painter()
    for _ in range(6):
        painter.paint(1)
        painter.move(1)
    assert painter.get_count() == 4