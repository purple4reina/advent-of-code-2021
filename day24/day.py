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
    funcs = [func00, func01, func02, func03, func04, func05, func06, func07,
            func08, func09, func10, func11, func12, func13]
    ws = [0] * 14

    @memoize
    def search(z_out, i):
        print('z_out,i: ', z_out,i)
        func = funcs[i]
        for w in range(9, 0, -1):
            ws[i] = w
            for z_in in range(10**6):
                if func(w, z_in) == z_out:
                    if i == 0:
                        print('ws: ', ws)
                        return True
                    if search(z_in, i - 1):
                        return True
        return False

    search(0, 13)
    return ws

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
