import day01
import pytest

def test_day01_2():
    result = day01.day01_2([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    assert result == 5, result
