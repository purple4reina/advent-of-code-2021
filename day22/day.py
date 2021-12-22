import numpy as np

def part1(steps):
    reactor = np.zeros((101, 101, 101), dtype=int)
    for action, regions in steps:
        section = []
        for axis, (start, end) in enumerate(regions):
            start, end = start + 50, end + 50 + 1
            section.append(slice(start, end))
        reactor[tuple(section)] = action
    return reactor.sum()

def part2(steps):
    total, prev_steps, new_prev_steps = 0, [], []
    for step, (action, ranges) in enumerate(steps):
        prev_steps, new_prev_steps = new_prev_steps, []
        (xs, xe), (ys, ye), (zs, ze) = ranges
        if action:
            total += (xe - xs + 1) * (ye - ys + 1) * (ze - zs + 1)
            new_prev_steps.append((-1, ranges))
        for paction, pranges in prev_steps:
            new_prev_steps.append((paction, pranges))
            (pxs, pxe), (pys, pye), (pzs, pze) = pranges
            mxe, mxs = min(xe, pxe), max(xs, pxs)
            mye, mys = min(ye, pye), max(ys, pys)
            mze, mzs = min(ze, pze), max(zs, pzs)
            if mxe > mxs and mye > mys and mze > mzs:
                total += (mxe - mxs + 1) * (mye - mys + 1) * \
                        (mze - mzs + 1) * paction
                new_prev_steps.append((-paction,
                    ((mxs, mxe), (mys, mye), (mzs, mze))))
    return total

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    steps = []
    for line in raw.split('\n'):
        step = []
        line = line.strip()
        step.append(int(line.startswith('on')))
        regions = []
        for region in line.split()[1].split(','):
            start, stop = map(int, region.split('=')[1].split('..'))
            regions.append((start, stop))
        step.append(regions)
        steps.append(step)
    return steps

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
