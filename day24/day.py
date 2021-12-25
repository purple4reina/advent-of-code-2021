def validate(n):
    num = []
    while n:
        n, r = divmod(n, 10)
        if r == 0:
            return False
        num.append(r)

    w = x = y = z = 0

    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 15
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 4
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 14
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 16
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -13
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 3
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 14
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 11
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 15
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -7
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 11
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 10
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 7
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -12
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 12
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 15
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 15
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -16
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -9
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 1
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -8
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 15
    y *= x
    z += y
    w = num.pop(0)
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -8
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 4
    y *= x
    z += y

    return z

def part1(instructions):

    for num in range(10**14-1, 0, -1):
        val = validate(num)
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
