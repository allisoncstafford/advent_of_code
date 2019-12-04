from day3_pt1 import get_pts, get_closest_intersection_pt_dist

def test_up():
    """Tests get_pts's ability to plot upward directions
    """
    assert get_pts(['U3']) == [(0,0), (0,1), (0,2), (0,3)], \
        "Should be [(0,0), (0,1), (0,2), (0,3)]"


def test_down():
    """Tests get_pts's abililty to plot downward directions
    """
    assert get_pts(['D3']) == [(0,0), (0,-1), (0,-2), (0,-3)], \
        "Should be [(0,0), (0,1), (0,2), (0,3)]"


def test_right():
    """Tests get_pts's abililty to plot rightward directions
    """
    assert get_pts(['R3']) == [(0,0), (1,0), (2,0), (3,0)], \
        "Should be [(0,0), (0,1), (0,2), (0,3)]"


def test_left():
    """Tests get_pts's abililty to plot leftward directions
    """
    assert get_pts(['L3']) == [(0,0), (-1,0), (-2,0), (-3,0)], \
        "Should be [(0,0), (0,1), (0,2), (0,3)]"


def test_multidirections():
    """Tests get_pts' ability to plot direction sequence
    """
    assert get_pts(['R3', 'U3']) == [(0,0), (1,0), (2,0), (3,0), (3,1), (3,2), (3,3)], \
        "Should be [(0,0), (1,0), (2,0), (3,0), (3,1), (3,2), (3,3)]"


def test_short_paths():
    """Tests get_closest_intersection_pt_dist with two short paths
    """
    assert get_closest_intersection_pt_dist(('R8','U5','L5','D3'), 
                                            ('U7','R6','D4','L4')) == 6, \
        "Should be 6."


def test_paths_w_long_segments():
    """Tests get_closest_intersection_pt_dist with paths that have segment
    lengths >9.
    """
    assert get_closest_intersection_pt_dist(('R75','D30','R83','U83','L12',
                                                'D49','R71','U7','L72'), 
                                            ('U62','R66','U55','R34','D71',
                                                'R55','D58','R83')) == 159, \
        "Should be 159."


def test_paths_w_negative_pts():
    """Tests get_closest_intersection_pt_dist with points in the 2nd and 3rd
    quadrants.
    """
    assert get_closest_intersection_pt_dist(('R98','U47','R26','D63','R33',
                                        'U87','L62','D20','R33','U53','R51'
                                        ),
                                        ('U98','R91','D20','R16','D67','R40',
                                        'U7','R15','U6','R7')
                                    ) == 135, \
                                                "Should be 135"