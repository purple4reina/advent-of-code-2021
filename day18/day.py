def magnitude(num):
    if isinstance(num, int):
        return num
    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])

def part1(inputs):
    pass

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    return list(map(int, raw.split()))

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
