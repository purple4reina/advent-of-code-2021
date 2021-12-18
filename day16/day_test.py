import pytest
from day import part1, part2, process

_test_part1 = (
        ('D2FE28', 6),
        ('38006F45291200', 9),
        ('EE00D40C823060', 14),
        ('8A004A801A8002F478', 16),
        ('620080001611562C8802118E34', 12),
        ('C0015000016115A2E0802F182340', 23),
        ('A0016C880162017C3686B18A3D4780', 31),
)

@pytest.mark.parametrize('raw,expect', _test_part1)
def test_part1(raw, expect):
    inputs = process(raw)
    assert expect == part1(inputs)
