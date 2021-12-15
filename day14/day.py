def part1(inputs):
    string, mutations = inputs

    for step in range(10):
        new_string = ''
        prev = ''
        for s in string:
            key = prev + s
            new_string += mutations.get(key, '')
            new_string += s
            prev = s
        string = new_string

    values = {}
    for s in string:
        values[s] = values.get(s, 0) + 1
    values = values.values()
    return max(values) - min(values)

def part2(inputs):
    string, mutations = inputs
    strs, counts = {}, {}
    for i in range(len(string) - 1):
        key = string[i:i+2]
        strs[key] = strs.get(key, 0) + 1
    for s in string:
        counts[s] = counts.get(s, 0) + 1

    for step in range(40):
        new_strs = {}
        for key, count in strs.items():
            middle = mutations.get(key)
            if middle:
                left, right = key
                new_strs[left+middle] = new_strs.get(left+middle, 0) + count
                new_strs[middle+right] = new_strs.get(middle+right, 0) + count
                counts[middle] = counts.get(middle, 0) + count
            else:
                new_strs[key] = new_strs.get(key, 0) + count
        strs = new_strs

    values = counts.values()
    return max(values) - min(values)

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    string, _, raw = raw.split('\n', 2)
    mutations = {}
    for line in raw.split('\n'):
        key, val = line.split(' -> ')
        mutations[key] = val
    return string, mutations

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
