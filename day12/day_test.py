import pytest
from day import part1, part2, process

_test_part1 = (
        ("""
        start-A
        start-b
        A-c
        A-b
        b-d
        A-end
        b-end
        """.strip(), 10),
        ("""
        dc-end
        HN-start
        start-kj
        dc-start
        dc-HN
        LN-dc
        HN-end
        kj-sa
        kj-HN
        kj-dc
        """.strip(), 19),
        ("""
        fs-end
        he-DX
        fs-he
        start-DX
        pj-DX
        end-zg
        zg-sl
        zg-pj
        pj-he
        RW-he
        fs-DX
        pj-RW
        zg-RW
        start-pj
        he-WI
        zg-he
        pj-fs
        start-RW
        """.strip(), 226),
)
_test_part1_ids = lambda a: a if isinstance(a, int) else 'raw'

@pytest.mark.parametrize('raw,expect', _test_part1,
        ids=_test_part1_ids)
def test_part1(raw, expect):
    inputs = process(raw)
    assert expect == part1(inputs)

_test_part2 = (
        ("""
        start-A
        start-b
        A-c
        A-b
        b-d
        A-end
        b-end
        """.strip(), 36),
        ("""
        dc-end
        HN-start
        start-kj
        dc-start
        dc-HN
        LN-dc
        HN-end
        kj-sa
        kj-HN
        kj-dc
        """.strip(), 103),
        ("""
        fs-end
        he-DX
        fs-he
        start-DX
        pj-DX
        end-zg
        zg-sl
        zg-pj
        pj-he
        RW-he
        fs-DX
        pj-RW
        zg-RW
        start-pj
        he-WI
        zg-he
        pj-fs
        start-RW
        """.strip(), 3509),
)
_test_part2_ids = lambda a: a if isinstance(a, int) else 'raw'

@pytest.mark.parametrize('raw,expect', _test_part2,
        ids=_test_part2_ids)
def test_part2(raw, expect):
    inputs = process(raw)
    assert expect == part2(inputs)
