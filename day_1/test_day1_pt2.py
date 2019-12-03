from day1_pt2 import fuel_counter_inc_fuel


def test_14():
    """Test that it can calculate fuel for mass 14."""
    assert fuel_counter_inc_fuel([14]) == 2, "Should be 2"


def test_1969():
    """Test that it can calculate fuel for mass 1969."""
    assert fuel_counter_inc_fuel([1969]) == 966, "Should be 966"


def test_100756():
    """Test that it can calculate fuel for mass 100756."""
    assert fuel_counter_inc_fuel([100756]) == 50346, "Should be 50346"

def test_12_14():
    """Test that it can calculate fuel for a list."""
    assert fuel_counter_inc_fuel([12, 14]) == 4, "Should be 4"