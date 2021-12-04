import numpy as np

def part1(inputs):
    nums, boards = inputs
    for num in nums:
        boards[boards==num] = 0
        for board in boards:
            if (board.sum(axis=0) == 0).any() or \
                    (board.sum(axis=1) == 0).any():
                return board.sum() * num

def part2(inputs):
    nums, boards = inputs
    new_boards = []
    for num in nums:
        boards[boards==num] = 0
        for board in boards:
            if (board.sum(axis=0) != 0).all() and \
                    (board.sum(axis=1) != 0).all():
                new_boards.append(board)
        if not len(new_boards):
            return board.sum() * num
        boards, new_boards = np.array(new_boards), []

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    numstr, boardstr = raw.split('\n', maxsplit=1)
    nums = [int(n) for n in numstr.split(',')]
    boards = []
    for b in boardstr.split('\n\n'):
        boards.append([
            [int(d) for d in l.split()]
            for l in b.split('\n') if l
        ])
    return nums, np.array(boards)

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
