import numpy as np

def part1(inputs):
    top = inputs.max() + 1
    floor = np.array([[0]*top for i in range(top)])
    for x1, y1, x2, y2 in inputs:
        if x1 == x2:
            for y in range(y1, y2 + 1):
                floor[y,x1] += 1
            for y in range(y2, y1 + 1):
                floor[y,x1] += 1
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                floor[y1,x] += 1
            for x in range(x2, x1 + 1):
                floor[y1,x] += 1
    return (floor > 1).sum()

def part2(inputs):
    top = inputs.max() + 1
    floor = np.array([[0]*top for i in range(top)])
    for x1, y1, x2, y2 in inputs:
        if x1 == x2:
            for y in range(y1, y2 + 1):
                floor[y,x1] += 1
            for y in range(y2, y1 + 1):
                floor[y,x1] += 1
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                floor[y1,x] += 1
            for x in range(x2, x1 + 1):
                floor[y1,x] += 1
        else:
            if x1 > x2:
                xrange = range(x1, x2 - 1, -1)
            else:
                xrange = range(x1, x2 + 1)
            if y1 > y2:
                yrange = range(y1, y2 - 1, -1)
            else:
                yrange = range(y1, y2 + 1)
            for x, y in zip(xrange, yrange):
                floor[y,x] += 1
    return (floor > 1).sum()

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    points = []
    for line in raw.split('\n'):
        a, b = line.split(' -> ')
        x1, y1 = a.split(',')
        x2, y2 = b.split(',')
        points.append((int(x1), int(y1), int(x2), int(y2)))
    return np.array(points)

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
