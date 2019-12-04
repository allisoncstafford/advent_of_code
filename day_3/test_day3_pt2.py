from day3_pt2 import get_shortest_step_ct

def test_short_paths():
    """Tests get_closest_intersection_pt_dist with two short paths
    """
    assert get_shortest_step_ct(('R8','U5','L5','D3'), 
                                            ('U7','R6','D4','L4')) == 30, \
        "Should be 30."


def test_paths_w_long_segments():
    """Tests get_closest_intersection_pt_dist with paths that have segment
    lengths >9.
    """
    assert get_shortest_step_ct(('R75','D30','R83','U83','L12',
                                                'D49','R71','U7','L72'), 
                                            ('U62','R66','U55','R34','D71',
                                                'R55','D58','R83')) == 610, \
        "Should be 610."


def test_paths_w_negative_pts():
    """Tests get_closest_intersection_pt_dist with points in the 2nd and 3rd
    quadrants.
    """
    assert get_shortest_step_ct(('R98','U47','R26','D63','R33',
                                        'U87','L62','D20','R33','U53','R51'
                                        ),
                                        ('U98','R91','D20','R16','D67','R40',
                                        'U7','R15','U6','R7')
                                    ) == 410, \
                                                "Should be 410"