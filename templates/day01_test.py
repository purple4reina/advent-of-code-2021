import pytest
from day01 import part1, part2

_test_part1 = (
)

@pytest.mark.parametrize('n,expect', _test_part1)
def test_part1(n, expect):
    assert expect == part1(n)

_test_part2 = (
)

@pytest.mark.parametrize('n,expect', _test_part2)
def test_part2(n, expect):
    assert expect == part2(n)
