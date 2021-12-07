import pytest
from day import part1, part2, process

_test_input = """
16,1,2,0,4,2,7,1,2,14
""".strip()
_test_part1_expect = 37
_test_part2_expect = 168

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)
