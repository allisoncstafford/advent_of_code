from d12_pt2 import extract_positions, apply_gravity, apply_velocities

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
    pos_vels = [1,2,4,3,0,0,0,0]
    pos_vels = apply_gravity(pos_vels)
    assert pos_vels[4:] == [3, 1, -3, -1]


def test_apply_velocities():
    lines = ['<x=-1, y=0, z=2>', 
        '<x=2, y=-10, z=-7>', 
        '<x=4, y=-8, z=8>', 
        '<x=3, y=5, z=-1>']
    pos_vels = extract_positions(lines)
    pos_vels.extend([0] * 12)
    pos_vels = apply_gravity(pos_vels)
    pos_vels = apply_velocities(pos_vels)
    assert pos_vels[0:4] == [2,3,1,2]

# def test_d12_pt2_main():
#     # read input positions
#     # lines = read_input('input.txt')
#     lines = ['<x=-1, y=0, z=2>', 
#         '<x=2, y=-10, z=-7>', 
#         '<x=4, y=-8, z=8>', 
#         '<x=3, y=5, z=-1>']
#     pos_vels = extract_positions(lines)

#     # add starting velocities to positions
#     pos_vels.extend([0]*12)

#     # start counter
#     count = 0

#     # start previous states list
#     previous_states = []

#     # step through until positions and velocities match a previous state
#     while True:
#         print(count, pos_vels)
#         previous_states.append(pos_vels.copy())
#         pos_vels  = apply_gravity(pos_vels)
#         pos_vels = apply_velocities(pos_vels)
#         count += 1
#         if pos_vels in previous_states:
#             print(count)
#             break
    
#     assert count == 2772


# def test_d12_pt2_main2():
#     lines = ['<x=-8, y=-10, z=0>',
#         '<x=5, y=5, z=10>',
#         '<x=2, y=-7, z=3>',
#         '<x=9, y=-8, z=-3>']
#     pos_vels = extract_positions(lines)

#     # add starting velocities to positions
#     pos_vels.extend([0]*12)

#     # start counter
#     count = 0

#     # start previous states list
#     previous_states = []

#     # step through until positions and velocities match a previous state
#     while True:
#         print(count, pos_vels)
#         previous_states.append(pos_vels.copy())
#         pos_vels  = apply_gravity(pos_vels)
#         pos_vels = apply_velocities(pos_vels)
#         count += 1
#         if pos_vels in previous_states:
#             print(count)
#             break
    
#     assert count == 4686774924