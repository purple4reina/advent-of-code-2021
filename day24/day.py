def part1(instructions):

    glbs = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in range(-99, 100):
        glbs[str(i)] = i

    def validate(n):
        num = []
        while n:
            n, r = divmod(n, 10)
            if r == 0:
                return False
            num.append(r)
        glbs['w'] = glbs['x'] = glbs['y'] = glbs['z'] = 0

        for instruction in instructions:
            fn, ab = instruction.split(' ', 1)
            if fn == 'inp':
                glbs[ab] = num.pop(0)
                continue
            a, b = ab.split()
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

        return glbs['z'] == 0

    for num in range(10**14, 0, -1):
        if num % 10**4 == 0: print('num: ', num)
        if validate(num):
            return num

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    instructions = []
    for line in raw.split('\n'):
        instructions.append(line)
    return tuple(instructions)

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
