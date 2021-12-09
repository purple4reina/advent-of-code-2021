def memoize(fn):
    _cache = {}
    def wrap(*args):
        if args in _cache:
            return _cache[args]
        ret = fn(*args)
        _cache[args] = ret
        return ret
    return wrap

def part1(matrix):

    h = len(matrix)
    w = len(matrix[0])

    def lowest(i, j):
        height = matrix[i][j]
        if i > 0 and matrix[i-1][j] < height:
            return False
        if i < h - 1 and matrix[i+1][j] < height:
            return False
        if j > 0 and matrix[i][j-1] < height:
            return False
        if j < w - 1 and matrix[i][j+1] < height:
            return False
        return True

    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if lowest(i, j):
                total += 1 + matrix[i][j]
    return total

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    matrix = []
    for line in raw.split():
        matrix.append(list(map(int, line)))
    return matrix

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
