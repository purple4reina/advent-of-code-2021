import os
import numpy as np
import time

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

    esc = '\033[0m'
    color = {
        1: '\033[48;2;0;0;0m',
        2: '\033[48;2;25;0;51m',
        3: '\033[48;2;51;0;102m',
        4: '\033[48;2;76;0;153m',
        5: '\033[48;2;102;0;204m',
        6: '\033[48;2;127;0;255m',
        7: '\033[48;2;153;51;255m',
        8: '\033[48;2;178;102;255m',
        9: '\033[48;2;204;153;255m',
        0: '\033[48;2;229;204;255m',
    }
    def draw():
        os.system('clear')
        for row in matrix:
            for octo in row:
                print(color[octo], end='')
                print('  ', end='')
                print(esc, end='')
            print()
        print(steps)
        time.sleep(0.01)

    steps = 0
    draw()
    while True:
        steps += 1
        prev = matrix > 9
        matrix += 1
        now = matrix > 9
        while (prev != now).any():
            for i in range(height):
                for j in range(width):
                    if now[i,j] and not prev[i,j]:
                        increase_neighbors(matrix, i, j)
            prev, now = now, matrix > 9
        matrix[now] = 0
        draw()
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
    print(part1(inputs.copy()))
    print(part2(inputs.copy()))
