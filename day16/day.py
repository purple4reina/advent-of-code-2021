def part1(msg):
    bits, bitmod, versions = 0, 1, 0
    for d in msg:
        i = int(d, 16)
        bits <<= 4
        bits += i
        bitmod <<= 4
    return parse_message(bits, bitmod)[0]

def parse_message(bits, bitmod):
    bitmod >>= 3
    versions, bits = divmod(bits, bitmod)

    bitmod >>= 3
    type_id, bits = divmod(bits, bitmod)

    if type_id == 4:
        num = 0
        while True:
            bitmod >>= 5
            numbits, bits = divmod(bits, bitmod)
            num <<= 4
            key, numbits = divmod(numbits, 16)
            num += numbits
            if not key:
                return versions, bits, bitmod, num

    bitmod >>= 1
    length_type_id, bits = divmod(bits, bitmod)
    nums = []

    if length_type_id:
        bitmod >>= 11
        subpacket_count, bits = divmod(bits, bitmod)
        for _ in range(subpacket_count):
            version, bits, bitmod, num = parse_message(bits, bitmod)
            versions += version
            nums.append(num)

    else:
        bitmod >>= 15
        subpacket_length, bits = divmod(bits, bitmod)
        bitmod >>= subpacket_length
        subbits, bits = divmod(bits, bitmod)
        subbitmod = 1 << subpacket_length
        while subbits:
            version, subbits, subbitmod, num = parse_message(subbits, subbitmod)
            versions += version
            nums.append(num)

    if type_id == 0:
        num = sum(nums)
    if type_id == 1:
        num = 1
        for n in nums:
            num *= n
    if type_id == 2:
        num = min(nums)
    if type_id == 3:
        num = max(nums)
    if type_id == 5:
        num = int(nums[0] > nums[1])
    if type_id == 6:
        num = int(nums[0] < nums[1])
    if type_id == 7:
        num = int(nums[0] == nums[1])

    return versions, bits, bitmod, num

def part2(msg):
    bits, bitmod, versions = 0, 1, 0
    for d in msg:
        i = int(d, 16)
        bits <<= 4
        bits += i
        bitmod <<= 4
    return parse_message(bits, bitmod)[-1]

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    return raw

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
