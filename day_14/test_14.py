from d14 import parse_rxns

def test_parse_rxns():
    lines = ['10 ORE => 10 A', '1 ORE => 1 B', '7 A, 1 B => 1 C', 
            '7 A, 1 C => 1 D', '7 A, 1 D => 1 E', '7 A, 1 E => 1 FUEL']
    elems = parse_rxns(lines)
    assert elems['FUEL']['n_out'] == 1
    assert elems['FUEL']['inputs'] == [[7, 'A'], [1, 'E']]