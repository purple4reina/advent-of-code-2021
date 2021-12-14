import numpy as np

def part1(inputs):
    matrix, folds = inputs
    for axis, val in folds:
        a, _, b = np.split(matrix, [val, val + 1], axis=axis)
        b = np.flip(b, axis=axis)

        ashape, bshape = a.shape[axis], b.shape[axis]
        base = a if ashape >= bshape else b
        add = b if ashape >= bshape else a

        ashape, bshape = add.shape[axis], base.shape[axis]
        slc = slice(bshape - ashape, bshape)
        if axis == 0:
            base[slc] += add
        else:
            base[:,slc] += add
        matrix = base
        break
    return (matrix > 0).sum()

def part2(inputs):

    matrix, folds = inputs
    for axis, val in folds:
        a, _, b = np.split(matrix, [val, val + 1], axis=axis)
        b = np.flip(b, axis=axis)

        ashape, bshape = a.shape[axis], b.shape[axis]
        base = a if ashape >= bshape else b
        add = b if ashape >= bshape else a

        ashape, bshape = add.shape[axis], base.shape[axis]
        slc = slice(bshape - ashape, bshape)
        if axis == 0:
            base[slc] += add
        else:
            base[:,slc] += add
        matrix = base

    return code(matrix)

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def code(matrix):
    code = ''
    for m in matrix:
        for d in m:
            code += '#' if d else ' '
        code += '\n'
    return code

def process(raw):
    dots, folds = [], []
    for line in raw.split('\n'):
        if not line:
            continue
        elif line.startswith('fold along'):
            axis, val = line.lstrip('fold along ').split('=')
            folds.append((0 if axis == 'y' else 1, int(val)))
        else:
            dots.append(tuple(map(int, line.split(','))))
    dots = np.array(dots)

    matrix = np.zeros((dots.max() + 1, dots.max() + 1))
    for x, y in dots:
        matrix[y,x] = 1

    # remove extra rows
    while matrix[-1].sum() == 0:
        matrix = matrix[:-1]

    # remove extra columns
    while matrix[:,-1].sum() == 0:
        matrix = matrix[:,:-1]

    return matrix, folds

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
