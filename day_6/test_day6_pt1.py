from day6_pt1 import t

def test_orbit_counting():
    example_lines = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H","D)I",
                     "E)J", "J)K", "K)L"]
    assert t(example_lines) == 42