from day7_pt1 import get_permutations, intcode_comp, calculate_output, t

def test_get_permutations():
    assert get_permutations(1, 3) == [(1, 2, 3), (1, 3, 2), (2, 1, 3),
                                    (2, 3, 1), (3, 1, 2), (3, 2, 1)], "Should be ((1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1))"

def test_intcode_comp():
    puzzle = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    assert intcode_comp(puzzle, 0, 4321) == 43210


def test_calc_output():
    puzzle = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    assert calculate_output([4,3,2,1,0], puzzle) == 43210


def test_main1():
    puzzle = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    assert t(puzzle) == 43210


def test_main2():
    puzzle = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
                101,5,23,23,1,24,23,23,4,23,99,0,0]
    assert t(puzzle) == 54321


def test_main3():
    puzzle = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
                1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    assert t(puzzle) == 65210