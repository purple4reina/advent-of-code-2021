def magnitude(num):
    if isinstance(num, int):
        return num
    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])

def add(num1, num2):
    num = [num1, num2]
    while True:
        exp = explode(num)
        if exp != num:
            num = exp
            continue
        spl = split(num)
        if spl != num:
            num = spl
            continue
        break
    return num

def is_regular_pair(num):
    if isinstance(num, int):
        return False
    return isinstance(num[0], int) and isinstance(num[1], int)

def explode(num):

    numstr = str(num).replace(' ', '')
    _replaced = [numstr]
    _digits = {str(i): True for i in range(10)}

    def find_correct_split(node_str):
        splits = numstr.split(node_str)
        if len(splits) == 2:
            return splits
        split = ''
        for i, spl in enumerate(splits[:-1]):
            split += spl
            lbracs = split.count('[')
            rbracs = split.count(']')
            if lbracs - rbracs == 4:
                break
            split += node_str
        left, right = split, node_str.join(splits[i+1:])
        return left, right

    def replace(num):
        node_str = str(num).replace(' ', '')
        left, right = find_correct_split(node_str)
        left_len, right_len = len(left), len(right)

        new_right = ''
        for i, s in enumerate(right):
            if _digits.get(s):
                nstr = ''
                while i < right_len and _digits.get(right[i]):
                    nstr += right[i]
                    i += 1
                nstr = str(int(nstr) + num[1])
                new_right += nstr
                i -= 1
                break
            new_right += s
        new_right += right[i+1:]

        new_left, left = '', left[::-1]
        for i, s in enumerate(left):
            if _digits.get(s):
                nstr = ''
                while i < left_len and _digits.get(left[i]):
                    nstr += left[i]
                    i += 1
                nstr = str(int(nstr[::-1]) + num[0])[::-1]
                new_left += nstr
                i -= 1
                break
            new_left += s
        new_left += left[i+1:]
        new_left = new_left[::-1]

        _replaced[0] = new_left + '0' + new_right

    def _explode(num, depth=0, exploded=False):
        if is_regular_pair(num) and depth > 3 and not exploded:
            replace(num)
            return True
        if isinstance(num, int):
            return exploded
        num1, num2 = num
        exploded = _explode(num1, depth=depth+1, exploded=exploded)
        exploded = _explode(num2, depth=depth+1, exploded=exploded)
        return exploded

    _explode(num)
    return eval(_replaced[0])

def split(num):

    def _split(num, split=False):
        if isinstance(num, int):
            if num > 9 and not split:
                return [num//2, num//2 + num%2], True
            return num, split
        num1, num2 = num
        num1spl, split = _split(num1, split)
        num2spl, split = _split(num2, split)
        return [num1spl, num2spl], split

    return _split(num)[0]

def part1(nums):
    num = nums.pop(0)
    while nums:
        num = add(num, nums.pop(0))
    return magnitude(num)

def part2(nums):
    num_len, largest = len(nums), 0
    for i in range(num_len):
        for j in range(num_len):
            if i == j:
                continue
            num = add(nums[i], nums[j])
            mag = magnitude(num)
            if mag > largest:
                largest = mag
    return largest

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    return [eval(l) for l in raw.split()]

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    inputs = process(read_inputs())
    print(part2(inputs))
