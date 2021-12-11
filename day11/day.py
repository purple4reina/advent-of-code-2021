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
    print('----------------------------------------')
    print('before step: ', 1)
    print(matrix)
    for step in range(100):
        print('----------------------------------------')
        matrix += 1
        octos = {}
        while True:
            flashed = 0
            now = matrix > 9
            #print()
            #print(matrix)
            for i in range(height):
                for j in range(width):
                    if now[i,j] and (i, j) not in octos:
                        increase_neighbors(matrix, i, j)
                        flashed += 1
                        flashes += 1
                        octos[(i, j)] = True
            if not flashed:
                break
        matrix[matrix>9] = 0
        print('after step: ', step+1)
        print(matrix)


        if step == 0:  # step 1
            expect = """
            6594254334
            3856965822
            6375667284
            7252447257
            7468496589
            5278635756
            3287952832
            7993992245
            5957959665
            6394862637
            """.replace('\n', '').replace(' ', '').strip()
            actual = ''.join([''.join(str(i) for i in m) for m in matrix])
            #assert expect == actual
        if step == 1:  # step 2
            expect = """
            8807476555
            5089087054
            8597889608
            8485769600
            8700908800
            6600088989
            6800005943
            0000007456
            9000000876
            8700006848
            """.replace('\n', '').replace(' ', '').strip()
            actual = ''.join([''.join(str(i) for i in m) for m in matrix])
            #assert expect == actual
        if step == 2:  # step 3
            expect = """
            0050900866
            8500800575
            9900000039
            9700000041
            9935080063
            7712300000
            7911250009
            2211130000
            0421125000
            0021119000
            """.replace('\n', '').replace(' ', '').strip()
            actual = ''.join([''.join(str(i) for i in m) for m in matrix])

            RED = '\033[0;31m'
            COLOR_OFF = '\033[0m'
            print('actual:')
            for i in range(height):
                for j in range(width):
                    if actual[i*width+j] != expect[i*width+j]:
                        print(RED, end='')
                    else:
                        print(COLOR_OFF, end='')
                    print(actual[i*width+j], end='')
                print()
            print(COLOR_OFF)
            print('expect:')
            for i in range(height):
                for j in range(width):
                    if actual[i*width+j] != expect[i*width+j]:
                        print(RED, end='')
                    else:
                        print(COLOR_OFF, end='')
                    print(expect[i*width+j], end='')
                print()
            print(COLOR_OFF)

            #assert expect == actual


    return flashes

def part2(inputs):
    pass

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
