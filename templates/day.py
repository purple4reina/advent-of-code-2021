def part1(inputs):
    pass

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return list(map(int, f.read().split()))

if __name__ == '__main__':
    inputs = read_inputs()
    print(part1(inputs))
