def part1(inputs):
    cave = [c.copy() for c in inputs]
    height = len(cave)
    width = len(cave[0])
    for i in range(height):
        for j in range(width):
            compares = []
            if i > 0:
                compares.append(cave[i-1][j])
            if j > 0:
                compares.append(cave[i][j-1])
            if compares:
                cave[i][j] += min(compares)
    return cave[-1][-1] - cave[0][0]

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
