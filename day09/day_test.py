import pytest
from day import part1, part2, process

_test_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()
_test_part1_expect = 15
_test_part2_expect = 1134

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)
