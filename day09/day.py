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

    @memoize
    def traverse(i, j):
        height = matrix[i][j]
        location = (i, j)

        if i > 0 and matrix[i-1][j] < height:
            height = matrix[i-1][j]
            location = (i-1, j)

        if i < h - 1 and matrix[i+1][j] < height:
            height = matrix[i+1][j]
            location = (i+1, j)

        if j > 0 and matrix[i][j-1] < height:
            height = matrix[i][j-1]
            location = (i, j-1)

        if j < w - 1 and matrix[i][j+1] < height:
            height = matrix[i][j+1]
            location = (i, j+1)

        if location != (i, j):
            return traverse(*location)
        return location

    minima = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            location = traverse(i, j)
            minima[location] = True

    return sum(matrix[i][j] for i, j in minima) + len(minima)

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
