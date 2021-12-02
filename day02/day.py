def part1(inputs):
    loc = [0, 0]
    for direction, speed in inputs:
        if direction == 'forward':
            loc[0] += speed
        elif direction == 'down':
            loc[1] += speed
        else:
            loc[1] -= speed
    return loc[0] * loc[1]

def part2(inputs):
    loc, aim = [0, 0], 0
    for direction, speed in inputs:
        if direction == 'forward':
            loc[0] += speed
            loc[1] += speed * aim
        elif direction == 'down':
            aim += speed
        else:
            aim -= speed
    return loc[0] * loc[1]

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    cmds = []
    raw = raw.strip()
    for line in raw.split('\n'):
        direction, speed = line.split()
        cmds.append((direction, int(speed)))
    return cmds

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
