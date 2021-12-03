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
    nums, leng = inputs
    matrix, new_matrix = [
            [
                int(bin(n)[2:].rjust(leng, '0')[i])
                for i in range(leng)
            ] for n in nums
    ], []
    for i in range(leng):
        most = sum(m[i] for m in matrix) >= len(matrix) / 2
        for m in matrix:
            if m[i] == most:
                new_matrix.append(m)
        matrix, new_matrix = new_matrix, []
        if len(matrix) == 1:
            o2 = int(''.join(map(str, matrix[0])), 2)
            break

    matrix, new_matrix = [
            [
                int(bin(n)[2:].rjust(leng, '0')[i])
                for i in range(leng)
            ] for n in nums
    ], []
    for i in range(leng):
        most = sum(m[i] for m in matrix) >= len(matrix) / 2
        for m in matrix:
            if m[i] != most:
                new_matrix.append(m)
        matrix, new_matrix = new_matrix, []
        if len(matrix) == 1:
            co2 = int(''.join(map(str, matrix[0])), 2)
            break

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
