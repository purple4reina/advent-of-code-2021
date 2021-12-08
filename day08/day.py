def part1(inputs):
    count = 0
    for _, outputs in inputs:
        for num in outputs:
            if len(num) in (2, 3, 4, 7):
                count += 1
    return count

def part2(puzzle_input):

    _translate = {
        0b1110111: 0, 0b0100100: 1, 0b1011101: 2, 0b1101101: 3, 0b0101110: 4,
        0b1101011: 5, 0b1111011: 6, 0b0100101: 7, 0b1111111: 8, 0b1101111: 9,
    }

    def digits_to_assign():
        return any(sum(v) > 1 for v in given_to_expected.values())

    def assign_digit(digit):
        length = len(digit)
        if length == 2:
            assign(digit, (0, 1, 3, 4, 6), (2, 5))
        elif length == 3:
            assign(digit, (1, 3, 4, 6), (0, 2, 5))
        elif length == 4:
            assign(digit, (0, 4, 6), (1, 2, 3, 5))
        elif length == 5:
            assign(digit, [], (0, 3, 6))
        elif length == 6:
            assign(digit, [], (0, 1, 5, 6))

    def assign(digit, outs, ins):
        for d in 'abcdefg':
            if d in digit:
                for i in outs:
                    given_to_expected[d][i] = 0
            else:
                for i in ins:
                    given_to_expected[d][i] = 0

    def clean_uniques():
        for key, values in given_to_expected.items():
            if sum(values) > 1:
                continue
            d = values.index(1)
            for other_key, other_values in given_to_expected.items():
                if key == other_key:
                    continue
                other_values[d] = 0

    def translate(digit):
        num = 0
        for d in digit:
            for i, j in enumerate(given_to_expected[d]):
                num += j << i
        return _translate[num]

    total = 0
    for inputs, outputs in puzzle_input:
        given_to_expected = {'a': [1]*7, 'b': [1]*7, 'c': [1]*7, 'd': [1]*7,
                'e': [1]*7, 'f': [1]*7, 'g': [1]*7}

        while digits_to_assign():
            for digit in inputs + outputs:
                assign_digit(digit)
            clean_uniques()

        num = 0
        for digit in outputs:
            num *= 10
            num += translate(digit)
        total += num

    return total

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    values = []
    for line in raw.split('\n'):
        inputs, outputs = line.split(' | ')
        values.append((inputs.split(), outputs.split()))
    return values

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
