from day10_pt2 import sort_astroids, set_laser, create_astroids
from day10_pt1 import get_best

def test_set_laser():
    lines = ['.#....#####...#..', '##...##.#####..##', '##...#...#.#####.',
            '..#.....#...###..', '..#.#.....#....##']
    astroids = create_astroids(lines)
    for astroid in astroids:
        astroid.set_n_detects(astroids)
    best_astroids = get_best(astroids)
    laser = best_astroids[0]
    set_laser(laser, astroids)
    assert astroids[0].angle_to_laser > 4.71
    assert astroids[0].angle_to_laser < 6.28
    assert round(astroids[0].dist_to_laser, 1) == 7.6

def test_sort_astroids():
    lines = ['.#....#####...#..', '##...##.#####..##', '##...#...#.#####.',
            '..#.....#...###..', '..#.#.....#....##']
    astroids = create_astroids(lines)
    for astroid in astroids:
        astroid.set_n_detects(astroids)
    best_astroids = get_best(astroids)
    laser = best_astroids[0]
    set_laser(laser, astroids)
    sorted_astroids = sort_astroids(laser, astroids)
    
    first = sorted_astroids[0]
    second = sorted_astroids[1]
    last = sorted_astroids[-1]

    assert (first.x, first.y) == (8, 1)
    assert (second.x, second.y) == (9, 0)
    assert (last.x, last.y) == (14, 3)


def test_sort_astroids2():
    lines = ['.#..##.###...#######', '##.############..##.', 
        '.#.######.########.#', '.###.#######.####.#.', 
        '#####.##.#.##.###.##', '..#####..#.#########', 
        '####################', '#.####....###.#.#.##', 
        '##.#################', '#####.##.###..####..',
        '..######..##.#######', '####.##.####...##..#',
        '.#####..#.######.###', '##...#.##########...',
        '#.##########.#######', '.####.#.###.###.#.##',
        '....##.##.###..#####', '.#.#.###########.###', 
        '#.#.#.#####.####.###', '###.##.####.##.#..##']
    astroids = create_astroids(lines)
    for astroid in astroids:
        astroid.set_n_detects(astroids)
    best_astroids = get_best(astroids)
    laser = best_astroids[0]
    set_laser(laser, astroids)
    sorted_astroids = sort_astroids(laser, astroids)
    
    first = sorted_astroids[0]
    second = sorted_astroids[1]
    third = sorted_astroids[2]
    tenth = sorted_astroids[9]
    twentieth= sorted_astroids[19]
    fiftieth = sorted_astroids[49]
    hundredth = sorted_astroids[99]
    one99 = sorted_astroids[198]
    two_hundo = sorted_astroids[199]
    two01 = sorted_astroids[200]
    last = sorted_astroids[-1]

    assert (first.x, first.y) == (11, 12)
    assert (second.x, second.y) == (12, 1)
    assert (third.x, third.y) == (12, 2)
    assert (tenth.x, tenth.y) == (12, 8)
    assert (twentieth.x, twentieth.y) == (16, 0)
    assert (fiftieth.x, fiftieth.y) == (16, 9)
    assert (hundredth.x, hundredth.y) == (10, 16)
    assert (one99.x, one99.y) == (9, 6)
    assert (two_hundo.x, two_hundo.y) == (8, 2)
    assert (two01.x, two01.y) == (10, 9)
    assert (last.x, last.y) == (11, 1)

    