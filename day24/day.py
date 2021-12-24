glbs = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
for i in range(-99, 100):
    glbs[str(i)] = i

def validate(instructions, n):
    num = []
    while n:
        n, r = divmod(n, 10)
        if r == 0:
            return False
        num.append(r)
    glbs['w'] = glbs['x'] = glbs['y'] = glbs['z'] = 0

    for fn, ab in instructions:
        if fn == 'inp':
            glbs[ab] = num.pop(0)
            continue
        a, b = ab
        if fn == 'add':
            glbs[a] += glbs[b]
        elif fn == 'mul':
            glbs[a] *= glbs[b]
        elif fn == 'eql':
            glbs[a] = int(glbs[a] == glbs[b])
        elif fn == 'mod':
            glbs[a] %= glbs[b]
        else:
            glbs[a] //= glbs[b]

    return glbs['z']

def part1(instructions):
    for num in range(10**14, 0, -1):
        val = validate(instructions, num)
        if val is False:
            continue
        if val == 0:
            return num

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    instructions = []
    for line in raw.split('\n'):
        fn, ab = line.split(' ', 1)
        inst = [fn]
        if fn == 'inp':
            inst.append(ab)
        else:
            inst.append(ab.split())
        instructions.append(inst)
    return instructions

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
