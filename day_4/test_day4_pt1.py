from day4_pt1 import meets_criteria

def test_pos():
    """tests that meets_criteria identify true case
    """
    assert meets_criteria(122345) == True, "Should be True"


def test_pos_2():
    """tests that meets_criteria identifies true case
    """
    assert meets_criteria(111123) == True, "Should be True"


def test_all_same():
    """tests that meets_criteria identifies single repeated number as true
    """
    assert meets_criteria(111111) == True, "Should be True"


def test_decrease():
    """tests that meets_criteria identifies decrease number as false
    """
    assert meets_criteria(223450) == False, "Should be False"


def test_no_double():
    """tests that meets_criteria identifies numbers without doubles as false
    """
    assert meets_criteria(123789) == False, "Should be False"

