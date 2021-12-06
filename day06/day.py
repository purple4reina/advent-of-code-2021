def part1(inputs):
    fish, new_fish = inputs, []
    for _ in range(80):
        for f in fish:
            if f == 0:
                new_fish.append(8)
                new_fish.append(6)
            else:
                new_fish.append(f - 1)
        fish, new_fish = new_fish, []
    return len(fish)

def part2(inputs):
    fish, new_fish = {i: 0 for i in range(9)}, {i: 0 for i in range(9)}
    for f in inputs:
        fish[f] += 1
    for _ in range(256):
        for f, n in fish.items():
            if f == 0:
                new_fish[8] += n
                new_fish[6] += n
            else:
                new_fish[f-1] += n
        fish, new_fish = new_fish, {i: 0 for i in range(9)}
    return sum(fish.values())

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    return list(map(int, raw.split(',')))

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
