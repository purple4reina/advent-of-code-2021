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
        while True:
            bitmod >>= 5
            num, bits = divmod(bits, bitmod)
            if not num // 16:
                return versions, bits, bitmod

    bitmod >>= 1
    length_type_id, bits = divmod(bits, bitmod)

    if length_type_id:
        bitmod >>= 11
        subpacket_count, bits = divmod(bits, bitmod)
        for _ in range(subpacket_count):
            version, bits, bitmod = parse_message(bits, bitmod)
            versions += version
    else:
        bitmod >>= 15
        subpacket_length, bits = divmod(bits, bitmod)
        bitmod >>= subpacket_length
        subbits, bits = divmod(bits, bitmod)
        subbitmod = 1 << subpacket_length
        while subbits:
            version, subbits, subbitmod = parse_message(subbits, subbitmod)
            versions += version

    return versions, bits, bitmod

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    return raw

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
