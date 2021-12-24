import pytest
from day import part1, part2, process, create_function

_test_create_instructions = (
        ("""
        inp w
        """.strip(), 2, 0),
        ("""
        inp w
        mul w -1
        """.strip(), 5, 0),
        ("""
        inp w
        add w 8
        """.strip(), 3, 0),
        ("""
        inp w
        add w 8
        add z w
        """.strip(), 3, 11),
)

@pytest.mark.parametrize('raw,inp,out', _test_create_instructions)
def test_create_instructions(raw, inp, out):
    func = create_function(process(raw)[0])
    print('func.__name__: ', func.__name__)
    assert out == func(inp)
