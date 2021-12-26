import pytest
from day import part1, part2, process

_test_input = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
""".strip()
_test_part1_expect = 12521
_test_part2_expect = 44169

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)
