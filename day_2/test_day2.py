from day2 import intcode


def test_add():
    """Test that intcode adds."""
    assert intcode([1,0,0,0,99]) == [2,0,0,0,99], "Should be [2,0,0,0,99]."


def test_multiply():
    """Test that intcode multiplies."""
    assert intcode([2,3,0,3,99]) == [2,3,0,6,99], "Should be [2,3,0,6,99]."


def test_returns_past_end_code():
    """Test that intcode returns values beyond the 99 end code."""
    assert intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801], \
        "Should be [2,4,4,5,99,9801]"
    
def test_two_actions():
    """Test that intcode works with multiple actions"""
    assert intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99], \
        "Should be [30,1,1,4,2,5,6,0,99]."