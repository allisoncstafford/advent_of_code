from day6_pt1 import t, build_tree
from day6_pt2 import get_prior_chain, count_distance

def test_orbit_counting():
    example_lines = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H","D)I",
                     "E)J", "J)K", "K)L"]
    assert t(example_lines) == 42


def test_get_prior_chain_basic():
    example_lines = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H","D)I",
                     "E)J", "J)K", "K)L"]
    planets = build_tree(example_lines)
    assert [x.name for x in get_prior_chain('C', planets)] == ['B', 'COM']


def test_get_prior_chain_branching():
    example_lines = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H","D)I",
                     "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]
    planets = build_tree(example_lines)
    assert [x.name for x in get_prior_chain('YOU', planets)] == ['K', 'J', 'E', 
                                                        'D', 'C', 'B', 'COM']


def test_count_distance():
    a = ['K', 'J', 'E', 'D', 'C', 'B', 'COM']
    b = ['I', 'D', 'C', 'B', 'COM']
    assert count_distance(a, b) == 4