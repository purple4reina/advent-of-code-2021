def part1(instructions):

    def validate(num):
        z = 0
        for digit, instr in zip(str(num), instructions):
            if digit == '0':
                return False
            z = create_function(instr, z=z)(digit)
        return z == 0

    top = 0
    for num in range(11111111111111, 10**14):
        if validate(num):
            top = num

    return top

def create_function(instructions, z=0):
    """
    inp w
    mul x 0
    add x z
    mod x 26
    div z 1
    add x 15
    eql x w
    eql x 0
    mul y 0
    add y 25
    mul y x
    add y 1
    mul z y
    mul y 0
    add y w
    add y 4
    mul y x
    add z y
    """

    def inp(fn):
        def _inp(w):
            glbs = {'w': int(w), 'x': 0, 'y': 0, 'z': z}
            for i in range(-99, 100):
                glbs[str(i)] = i
            return fn(glbs)
        return _inp

    def add(ab):
        a, b = ab.split()
        def _add(fn):
            def __add(glbs):
                glbs[a] = glbs[a] + glbs[b]
                return fn(glbs)
            return __add
        return _add

    def mul(ab):
        a, b = ab.split()
        def _mul(fn):
            def __mul(glbs):
                glbs[a] = glbs[a] + glbs[b]
                return fn(glbs)
            return __mul
        return _mul

    def div(ab):
        a, b = ab.split()
        def _div(fn):
            def __div(glbs):
                glbs[a] = glbs[a] // glbs[b]
                return fn(glbs)
            return __div
        return _div

    def mod(ab):
        a, b = ab.split()
        def _mod(fn):
            def __mod(glbs):
                glbs[a] = glbs[a] % glbs[b]
                return fn(glbs)
            return __mod
        return _mod

    def eql(ab):
        a, b = ab.split()
        def _eql(fn):
            def __eql(glbs):
                glbs[a] = int(glbs[a] == glbs[b])
                return fn(glbs)
            return __eql
        return _eql

    def func(glbs):
        return glbs['z']

    _funcs = {
            'inp': inp, 'add': add, 'mul': mul,
            'div': div, 'mod': mod, 'eql': eql,
    }

    for instruction in instructions[:0:-1]:
        f, ab = instruction.split(' ', 1)
        func = _funcs[f](ab)(func)

    return inp(func)

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    instructions, instruction = [], []
    for line in raw.split('\n'):
        if line.startswith('inp'):
            if instruction:
                instructions.append(instruction)
                instruction = []
        instruction.append(line.strip())
    instructions.append(instruction)
    return instructions

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
