import pytest
from day import part1, part2, process

_test_part1_input = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()
_test_part1_expect = 150

def test_part1():
    inputs = process(_test_part1_input)
    assert _test_part1_expect == part1(inputs)

_test_part2_input = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()
_test_part2_expect = 900

def test_part2():
    inputs = process(_test_part2_input)
    assert _test_part2_expect == part2(inputs)
