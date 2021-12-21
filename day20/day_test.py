import pytest
from day import part1, part2, process, read_inputs

_test_input = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
""".strip()
_test_part1_expect = 35
_test_part2_expect = 3351

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)

_test_not_part1 = (
        pytest.param(read_inputs(), 6039, id='my-puzzle-input'),  # too high
        pytest.param(read_inputs(), 5828, id='my-puzzle-input'),  # too high
        pytest.param(read_inputs(), 5619, id='my-puzzle-input'),  # too high
)

@pytest.mark.parametrize('raw,expect', _test_not_part1)
def test_not_part1(raw, expect):
    inputs = process(raw)
    assert expect != part1(inputs)

_test_not_part2 = (
        pytest.param(read_inputs(), 52212, id='my-puzzle-input'),  # too high
)

@pytest.mark.parametrize('raw,expect', _test_not_part2)
def test_not_part2(raw, expect):
    inputs = process(raw)
    assert expect != part2(inputs)
