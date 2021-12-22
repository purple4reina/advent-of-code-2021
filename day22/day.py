import numpy as np

def part1(steps):
    reactor = np.zeros((101, 101, 101), dtype=int)
    for action, regions in steps:
        section = []
        for axis, (start, end) in enumerate(regions):
            start, end = start + 50, end + 50 + 1
            section.append(slice(start, end))
        reactor[tuple(section)] = action
    return reactor.sum()

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    steps = []
    for line in raw.split('\n'):
        step = []
        line = line.strip()
        step.append(line.startswith('on'))
        regions = []
        for region in line.split()[1].split(','):
            start, stop = map(int, region.split('=')[1].split('..'))
            regions.append((start, stop))
        step.append(regions)
        steps.append(step)
    return steps

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
