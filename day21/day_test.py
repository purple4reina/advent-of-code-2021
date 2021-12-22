import pytest
from day import part1, part2, process

_test_input = """
Player 1 starting position: 4
Player 2 starting position: 8
""".strip()
_test_part1_expect = 739785
_test_part2_expect = 444356092776315

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)
