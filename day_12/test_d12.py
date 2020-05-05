from d12 import extract_positions, apply_gravity, apply_velocities, calc_energy

def test_extract_positions():
    lines = ['<x=-1, y=0, z=2>', 
            '<x=2, y=-10, z=-7>', 
            '<x=4, y=-8, z=8>', 
            '<x=3, y=5, z=-1>']
    assert extract_positions(lines) == [[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]]


def test_apply_gravity():
    lines = ['<x=-1, y=0, z=2>', 
        '<x=2, y=-10, z=-7>', 
        '<x=4, y=-8, z=8>', 
        '<x=3, y=5, z=-1>']
    pos = extract_positions(lines)
    vels = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    vels = apply_gravity(pos, vels)
    assert vels == [[3, -1, -1], [1, 3, 3], [-3, 1, -3], [-1, -3, 1]]


def test_apply_velocities():
    lines = ['<x=-1, y=0, z=2>', 
        '<x=2, y=-10, z=-7>', 
        '<x=4, y=-8, z=8>', 
        '<x=3, y=5, z=-1>']
    pos = extract_positions(lines)
    vels = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    vels = apply_gravity(pos, vels)
    pos = apply_velocities(pos, vels)
    assert pos == [[2,-1,1],[3,-7,-4],[1,-7,5],[2,2,0]]


def test_calc_energy():
    pos = [[2,1,-3], [1,-8,0], [3,-6,1], [2,0,4]]
    vels = [[-3,-2,1], [-1,1,3], [3,2,-3],[1,-1,-1]]
    assert calc_energy(pos, vels) == 179