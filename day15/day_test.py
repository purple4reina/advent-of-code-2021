import pytest
from day import part1, part2, process_part1, process_part2

_test_input = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip()
_test_part1_expect = 40
_test_part2_expect = 315

def test_part1():
    inputs = process_part1(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process_part2(_test_input)
    assert _test_part2_expect == part2(inputs)
