from d12_pt2 import (extract_positions, 
                    apply_gravity, 
                    apply_velocities,
                    parse_dimensions,
                    calc_cycle,
                    lcm)

def test_extract_positions():
    lines = ['<x=-1, y=0, z=2>', 
            '<x=2, y=-10, z=-7>', 
            '<x=4, y=-8, z=8>', 
            '<x=3, y=5, z=-1>']
    assert extract_positions(lines) == [-1,0,2,2,-10,-7,4,-8,8,3,5,-1]


def test_apply_gravity():
    # lines = ['<x=-1, y=0, z=2>', 
    #     '<x=2, y=-10, z=-7>', 
    #     '<x=4, y=-8, z=8>', 
    #     '<x=3, y=5, z=-1>']
    pos_vels_x = [-1,2,4,3,0,0,0,0]
    pos_vels_x = apply_gravity(pos_vels_x)
    assert pos_vels_x[4:] == [3, 1, -3, -1]


def test_apply_velocities():
    # lines = ['<x=-1, y=0, z=2>', 
    #     '<x=2, y=-10, z=-7>', 
    #     '<x=4, y=-8, z=8>', 
    #     '<x=3, y=5, z=-1>']
    pos_vels_x = [-1,2,4,3,0,0,0,0]
    pos_vels_x = apply_gravity(pos_vels_x)
    pos_vels_x = apply_velocities(pos_vels_x)
    assert pos_vels_x[0:4] == [2,3,1,2]

def test_d12_pt2_main():
    lines = ['<x=-1, y=0, z=2>', 
        '<x=2, y=-10, z=-7>', 
        '<x=4, y=-8, z=8>', 
        '<x=3, y=5, z=-1>']
    pos_vels = extract_positions(lines)

    # add starting velocities to positions
    pos_vels.extend([0]*12)

    x0s, y0s, z0s = parse_dimensions(pos_vels)

    # count cycle times
    x_cycle = calc_cycle(x0s)
    y_cycle = calc_cycle(y0s)
    z_cycle = calc_cycle(z0s)

    # find lowest common denomenator btwen x, y, z
    assert lcm(x_cycle, lcm(y_cycle, z_cycle)) == 2772


def test_d12_pt2_main2():
    lines = ['<x=-8, y=-10, z=0>',
        '<x=5, y=5, z=10>',
        '<x=2, y=-7, z=3>',
        '<x=9, y=-8, z=-3>']
    pos_vels = extract_positions(lines)

    # add starting velocities to positions
    pos_vels.extend([0]*12)

    x0s, y0s, z0s = parse_dimensions(pos_vels)

    # count cycle times
    x_cycle = calc_cycle(x0s)
    y_cycle = calc_cycle(y0s)
    z_cycle = calc_cycle(z0s)

    # find lowest common denomenator btwen x, y, z
    assert lcm(x_cycle, lcm(y_cycle, z_cycle)) == 4686774924