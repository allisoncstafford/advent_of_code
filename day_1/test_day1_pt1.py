from day1_pt1 import fuel_counter

def test_12():
    """Test that it can calculate fuel for mass 12."""
    assert fuel_counter([12]) == 2, "Should be 2"


def test_14():
    """Test that it can calculate fuel for mass 14."""
    assert fuel_counter([14]) == 2, "Should be 2"


def test_1969():
    """Test that it can calculate fuel for mass 1969."""
    assert fuel_counter([1969]) == 654, "Should be 654"


def test_100756():
    """Test that it can calculate fuel for mass 100756."""
    assert fuel_counter([100756]) == 33583, "Should be 33583"

def test_12_14():
    """Test that it can calculate fuel for a list."""
    assert fuel_counter([12, 14]) == 4, "Should be 4"