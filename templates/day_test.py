import pytest
from day import part1, part2, process

_test_part1_input = """
"""
_test_part1_expect = None

def test_part1():
    inputs = process(_test_part1_input)
    assert _test_part1_expect == part1(inputs)

_test_part2_input = """
"""
_test_part2_expect = None

def test_part2():
    inputs = process(_test_part2_input)
    assert _test_part2_expect == part2(inputs)
