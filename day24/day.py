def memoize(fn):
    _cache = {}
    def wrap(*args):
        if args in _cache:
            return _cache[args]
        ret = fn(*args)
        _cache[args] = ret
        return ret
    return wrap

@memoize
def func00(w, z):
    x = y = 0
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
    return z

@memoize
def func01(w, z):
    x = y = 0
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
    return z

@memoize
def func02(w, z):
    x = y = 0
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
    return z

@memoize
def func03(w, z):
    x = y = 0
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
    return z

@memoize
def func04(w, z):
    x = y = 0
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
    return z

@memoize
def func05(w, z):
    x = y = 0
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
    return z

@memoize
def func06(w, z):
    x = y = 0
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
    return z

@memoize
def func07(w, z):
    x = y = 0
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
    return z

@memoize
def func08(w, z):
    x = y = 0
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
    return z

@memoize
def func09(w, z):
    x = y = 0
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
    return z

@memoize
def func10(w, z):
    x = y = 0
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
    return z

@memoize
def func11(w, z):
    x = y = 0
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
    return z

@memoize
def func12(w, z):
    x = y = 0
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
    return z

@memoize
def func13(w, z):
    x = y = 0
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
    least = 10**14
    z_00 = 0
    for w_00 in range(9, 0, -1):
        z_01 = func00(w_00, z_00)
        for w_01 in range(9, 0, -1):
            z_02 = func01(w_01, z_01)
            for w_02 in range(9, 0, -1):
                z_03 = func02(w_02, z_02)
                for w_03 in range(9, 0, -1):
                    z_04 = func03(w_03, z_03)
                    for w_04 in range(9, 0, -1):
                        z_05 = func04(w_04, z_04)
                        for w_05 in range(9, 0, -1):
                            z_06 = func05(w_05, z_05)
                            for w_06 in range(9, 0, -1):
                                z_07 = func06(w_06, z_06)
                                print(w_00, w_01, w_02, w_03, w_04, w_05, w_06,
                                        least)
                                for w_07 in range(9, 0, -1):
                                    z_08 = func07(w_07, z_07)
                                    for w_08 in range(9, 0, -1):
                                        z_09 = func08(w_08, z_08)
                                        for w_09 in range(9, 0, -1):
                                            z_10 = func09(w_09, z_09)
                                            for w_10 in range(9, 0, -1):
                                                z_11 = func10(w_10, z_10)
                                                for w_11 in range(9, 0, -1):
                                                    z_12 = func11(w_11, z_11)
                                                    for w_12 in range(9, 0, -1):
                                                        z_13 = func12(w_12, z_12)
                                                        for w_13 in range(9, 0, -1):
                                                            z = func13(w_13, z_13)
                                                            if z < least:
                                                                least = z
                                                            if z == 0:
                                                                return (w_00,
                                                                        w_01,
                                                                        w_02,
                                                                        w_03,
                                                                        w_04,
                                                                        w_05,
                                                                        w_06,
                                                                        w_07,
                                                                        w_08,
                                                                        w_09,
                                                                        w_10,
                                                                        w_11,
                                                                        w_12,
                                                                        w_13)

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
