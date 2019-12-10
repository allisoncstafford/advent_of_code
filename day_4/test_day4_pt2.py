from day4_pt2 import meets_criteria2, exactly_two_same_digits

def test_exactly2_false():
    """tests for requiring one digit to be repeated exactly two consecutive
    times.
    """
    assert exactly_two_same_digits(123555) == False, "Should be True"


def test_exactly2_true():
    """tests for requiring one digit to be repeated exactly two consectutive
    tiems.
    """
    assert exactly_two_same_digits(112345) == True, "Should be True"

def test_3_consec():
    """tests for identifying a digit repeated three consecutive times as False.
    """
    assert exactly_two_same_digits(123444) == False, "Should be False"

def test_one2_another_multiple():
    """tests for identifying one double number with a different repeated number
    also as True.
    """
    assert exactly_two_same_digits(111122) == True, "Should be True"
