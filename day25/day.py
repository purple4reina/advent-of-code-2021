import numpy as np

def part1(inputs):

    def new_map():
        return np.zeros((height, width), dtype=int)

    east, south = inputs
    height, width = east.shape
    step, moved = 0, True

    while moved:
        step += 1
        moved = False

        new_east = new_map()

        for i in range(height):
            for j in range(width):
                if not east[i,j]:
                    continue
                k = (j + 1) % width
                if not east[i,k] and not south[i,k]:
                    moved = True
                    new_east[i,k] = 1
                else:
                    new_east[i,j] = 1

        east = new_east
        new_south = new_map()

        for i in range(height):
            for j in range(width):
                if not south[i,j]:
                    continue
                k = (i + 1) % height
                if not east[k,j] and not south[k,j]:
                    moved = True
                    new_south[k,j] = 1
                else:
                    new_south[i,j] = 1

        south = new_south

    return step

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    lines = raw.split()
    height, width = len(lines), len(lines[0])
    east = np.zeros((height, width), dtype=int)
    south = np.zeros((height, width), dtype=int)
    for i in range(height):
        for j in range(width):
            val = lines[i][j]
            if val == '>':
                east[i,j] = 1
            elif val == 'v':
                south[i,j] = 1
    return east, south

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
