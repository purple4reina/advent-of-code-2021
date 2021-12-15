import sys
sys.setrecursionlimit(10**5)

def memoize(fn):
    _cache = {}
    def wrap(*args):
        if args in _cache:
            return _cache[args]
        ret = fn(*args)
        _cache[args] = ret
        return ret
    return wrap

def part1(cave):

    height = len(cave)
    width = len(cave[0])

    neighbors_of = []
    for i in range(height):
        row = []
        for j in range(width):
            vals = []
            if j < width - 1:
                vals.append((i, j+1))
            if i < height - 1:
                vals.append((i+1, j))
            if j > 0:
                vals.append((i, j-1))
            if i > 0:
                vals.append((i-1, j))
            row.append(vals)
        neighbors_of.append(row)

    @memoize
    def search(i, j, total):
        if i == height - 1 and j == width - 1:
            if total < global_lowest[0]:
                global_lowest[0] = total
            return total
        if total >= global_lowest[0]:
            return float('inf')
        choices = []
        for k, l in neighbors_of[i][j]:
            val = search(k, l, total + cave[k][l])
            choices.append(val)
        return min(choices)

    global_lowest = [9 * height * width]
    return search(0, 0, 0)

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    return [[int(i) for i in row] for row in raw.split()]

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
