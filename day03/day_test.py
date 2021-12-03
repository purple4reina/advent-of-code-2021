import pytest
from day import part1, part2, process

_test_input = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()
_test_part1_expect = 198
_test_part2_expect = 230

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)
