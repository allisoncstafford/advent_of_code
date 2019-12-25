from day5_pt1 import parse_instruction

def test_parse_instruction0():
    assert parse_instruction([12345, 1, 2], 0)[0] == '45', "Should be last two digits"

def test_parse_instruction1():
    assert parse_instruction([12345, 1, 2], 0)[1] == [3, 2, 1], "Should be 3,2,1"

def test_parse_intruction2():
    assert parse_instruction([12345, 1, 2], 0)[2] == 1, "should be 1"