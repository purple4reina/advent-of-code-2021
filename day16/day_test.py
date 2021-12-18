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

_test_part2 = (
        ('D2FE28', 2021),
        ('C200B40A82', 3),
        ('04005AC33890', 54),
        ('880086C3E88112', 7),
        ('CE00C43D881120', 9),
        ('D8005AC2A8F0', 1),
        ('F600BC2D8F', 0),
        ('9C005AC2F8F0', 0),
        ('9C0141080250320F1802104A08', 1),
)

@pytest.mark.parametrize('n,expect', _test_part2)
def test_part2(n, expect):
    assert expect == part2(n)
