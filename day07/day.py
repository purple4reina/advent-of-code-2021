def part1(inputs):
    smallest = float('inf')
    for x in range(max(inputs) + 1):
        fuel = 0
        for inp in inputs:
            fuel += abs(x - inp)
        if fuel < smallest:
            smallest = fuel
    return smallest

def part2(inputs):

    def triangle(n):
        return n * (n + 1) // 2

    smallest = float('inf')
    for x in range(max(inputs) + 1):
        fuel = 0
        for inp in inputs:
            fuel += triangle(abs(x - inp))
        if fuel < smallest:
            smallest = fuel
    return smallest

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    return list(map(int, raw.split(',')))

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
