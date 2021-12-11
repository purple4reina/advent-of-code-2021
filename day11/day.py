import numpy as np

def part1(matrix):

    height, width = matrix.shape

    adjacency = []
    for i in range(height):
        adj = []
        for j in range(width):
            element = []
            if i > 0 and j > 0:
                element.append((i-1, j-1))
            if i > 0:
                element.append((i-1, j))
            if i > 0 and j < width - 1:
                element.append((i-1, j+1))
            if j < width - 1:
                element.append((i, j+1))
            if i < height - 1 and j < width - 1:
                element.append((i+1, j+1))
            if i < height - 1:
                element.append((i+1, j))
            if i < height - 1 and j > 0:
                element.append((i+1, j-1))
            if j > 0:
                element.append((i, j-1))
            adj.append(element)
        adjacency.append(adj)

    def increase_neighbors(matrix, i, j):
        for k, l in adjacency[i][j]:
            matrix[k,l] += 1

    flashes = 0
    for step in range(100):
        matrix += 1
        octos = {}
        while True:
            flashed = 0
            now = matrix > 9
            for i in range(height):
                for j in range(width):
                    if now[i,j] and (i, j) not in octos:
                        increase_neighbors(matrix, i, j)
                        flashed += 1
                        octos[(i, j)] = True
            flashes += flashed
            if not flashed:
                break
        matrix[matrix>9] = 0

    return flashes

def part2(matrix):

    height, width = matrix.shape

    adjacency = []
    for i in range(height):
        adj = []
        for j in range(width):
            element = []
            if i > 0 and j > 0:
                element.append((i-1, j-1))
            if i > 0:
                element.append((i-1, j))
            if i > 0 and j < width - 1:
                element.append((i-1, j+1))
            if j < width - 1:
                element.append((i, j+1))
            if i < height - 1 and j < width - 1:
                element.append((i+1, j+1))
            if i < height - 1:
                element.append((i+1, j))
            if i < height - 1 and j > 0:
                element.append((i+1, j-1))
            if j > 0:
                element.append((i, j-1))
            adj.append(element)
        adjacency.append(adj)

    def increase_neighbors(matrix, i, j):
        for k, l in adjacency[i][j]:
            matrix[k,l] += 1

    steps = 0
    while True:
        steps += 1
        prev = matrix > 9
        matrix += 1
        now = matrix > 9
        octos = {}
        while (prev != now).any():
            for i in range(height):
                for j in range(width):
                    if now[i,j] and not prev[i,j]:
                        increase_neighbors(matrix, i, j)
            prev, now = now, matrix > 9
        matrix[matrix>9] = 0
        if (matrix == 0).all():
            return steps

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    matrix = []
    for row in raw.split():
        line = []
        for d in row:
            line.append(int(d))
        matrix.append(line)
    return np.array(matrix)

if __name__ == '__main__':
    inputs = process(read_inputs())
    #inputs = process("""11111
    #        19991
    #        19191
    #        19991
    #        11111""".strip())
    print(part1(inputs))
    print(part2(inputs))
