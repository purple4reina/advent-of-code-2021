def part1(matrix):

    h = len(matrix)
    w = len(matrix[0])

    def lowest(i, j):
        height = matrix[i][j]
        if i > 0 and matrix[i-1][j] <= height:
            return False
        if i < h - 1 and matrix[i+1][j] <= height:
            return False
        if j > 0 and matrix[i][j-1] <= height:
            return False
        if j < w - 1 and matrix[i][j+1] <= height:
            return False
        return True

    total = 0
    for i in range(h):
        for j in range(w):
            if lowest(i, j):
                total += 1 + matrix[i][j]
    return total

def part2(matrix):

    h = len(matrix)
    w = len(matrix[0])

    def record_basin(i, j):
        if matrix[i][j] == 9:
            return
        visited = {}
        while True:
            height = matrix[i][j]

            if i > 0 and matrix[i-1][j] <= height:
                i, j = i-1, j
                if not visited.get((i, j)):
                    visited[(i, j)] = True
                    continue
            if i < h - 1 and matrix[i+1][j] <= height:
                i, j = i+1, j
                if not visited.get((i, j)):
                    visited[(i, j)] = True
                    continue
            if j > 0 and matrix[i][j-1] <= height:
                i, j = i, j-1
                if not visited.get((i, j)):
                    visited[(i, j)] = True
                    continue
            if j < w - 1 and matrix[i][j+1] <= height:
                i, j = i, j+1
                if not visited.get((i, j)):
                    visited[(i, j)] = True
                    continue

            break
        basin[i][j] += 1

    basin = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            record_basin(i, j)

    a, b, c = sorted([c for row in basin for c in row])[-3:]
    return a * b * c

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
