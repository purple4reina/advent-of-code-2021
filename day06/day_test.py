import pytest
from day import part1, part2, process

_test_input = """
3,4,3,1,2
""".strip()
_test_part1_expect = 5934
_test_part2_expect = 26984457539

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)
