import numpy as np

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
            return total
        choices = []
        for k, l in neighbors_of[i][j]:
            choices.append(search(k, l, total + cave[k][l]))
        return min(choices)

    global_lowest = [9 * height * width]
    return search(0, 0, 0)

def part2(cave):

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
    neighbors_of = np.array(neighbors_of, dtype=object)
    cave = np.array(cave)

    def smallest_unvisited():
        idx = np.flatnonzero(unvisited)
        return np.unravel_index(idx[np.take(distances, idx).argmin()],
                distances.shape)

    unvisited = np.ones((height, width))
    distances = np.full((height, width), height*width*10)
    distances[0,0] = unvisited[0,0] = i = j = 0

    while i < height - 1 or j < width - 1:
        current_distance = distances[i,j]
        for k, l in neighbors_of[i,j]:
            distances[k,l] = min(distances[k,l], current_distance + cave[k,l])
        unvisited[i,j] = False
        i, j = smallest_unvisited()

    return distances[i,j]

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process_part1(raw):
    return [[int(i) for i in row] for row in raw.split()]

def process_part2(raw):
    cave = []
    for row_repeat in range(5):
        for row in raw.split():
            new_row = []
            for col_repeat in range(5):
                for risk in row:
                    new_val = int(risk) + row_repeat + col_repeat
                    if new_val > 9:
                        new_val -= 9
                    new_row.append(new_val)
            cave.append(new_row)
    return cave

if __name__ == '__main__':
    inputs = process_part1(read_inputs())
    print(part1(inputs))
    inputs = process_part2(read_inputs())
    print(part2(inputs))
