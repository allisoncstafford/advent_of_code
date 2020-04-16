from intcode9 import IntcodeComp

def test_intcode1():
    code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    comp = IntcodeComp(code)
    assert comp.compute() == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

# def test_intcode2():
#     code = [1102,34915192,34915192,7,4,7,99,0]
#     comp = IntcodeComp(code)
#     assert comp.compute() == '16 digits'


# def test_intcode3():
#     code = [104,1125899906842624,99]
#     comp = IntcodeComp(code)
#     assert comp.compute() == 1125899906842624