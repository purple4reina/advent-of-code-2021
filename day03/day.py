def part1(inputs):
    nums, leng = inputs
    zeros, ones = [0]*leng, [0]*leng
    for num in nums:
        for i in range(leng):
            if num & 1:
                ones[i] += 1
            else:
                zeros[i] += 1
            num >>= 1
    gamma = epsilon = 0
    for i, (zero, one) in enumerate(zip(zeros, ones)):
        if one > zero:
            gamma += 1 << i
        else:
            epsilon += 1 << i
    return gamma * epsilon

def part2(inputs):

    def sieve(greatest):
        matrix, new_matrix = nums, []
        for i in range(leng):
            dig = leng - i - 1
            most = sum(m>>dig & 1 for m in matrix) >= len(matrix) / 2
            for m in matrix:
                if (m>>dig & 1 == most) is greatest:
                    new_matrix.append(m)
            matrix, new_matrix = new_matrix, []
            if len(matrix) == 1:
                return matrix[0]

    nums, leng = inputs
    o2 = sieve(True)
    co2 = sieve(False)
    return o2 * co2

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    inp, leng = [], 0
    for num in raw.split():
        inp.append(int(num, 2))
        if not leng:
            leng = len(num)
    return inp, leng

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
