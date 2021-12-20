import itertools
import numpy as np

def _rotations_2():
    R2_0 = np.array([[1, 0], [0, 1]])
    R2_1 = np.array([[0, 1], [-1, 0]])
    R2_2 = R2_1 @ R2_1
    R2_3 = R2_2 @ R2_1
    return [R2_0, R2_1, R2_2, R2_3]

# 3-dimensions
def _rotations_3():
    Rx = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    Ry = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])
    Rz = np.array([[1, 0, 0], [-1, 0, 0], [0, 0, 1]])
    I  = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    rotations = {}
    for rots in itertools.product(range(4), repeat=3):
        rot = I
        for x in range(rots[0]):
            rot = rot @ Rx
        for y in range(rots[1]):
            rot = rot @ Ry
        for z in range(rots[2]):
            rot = rot @ Rz
        rotations[str(rot)] = rot

    return list(rotations.values())

_rotations = {2: _rotations_2(), 3: _rotations_3()}

def part1(scanners, overlap=12):

    mapp = set(tuple(s) for s in scanners[0])
    dims = len(scanners[0][0])
    scanners, retry_scanners = [np.array(s) for s in scanners[1:]], []

    while len(scanners):
        for scanner in scanners:
            for rotation in ((r @ scanner.T).T for r in _rotations[dims]):

                distances = {}
                for m in mapp:
                    for r in rotation:
                        dist = tuple(m - r)
                        distances[dist] = distances.get(dist, 0) + 1

                max_count, max_distance = max((v,k) for k,v in distances.items())
                if max_count < overlap:
                    continue

                for r in rotation:
                    mapp.add(tuple(r + max_distance))
                break

            else:
                retry_scanners.append(scanner)
        scanners, retry_scanners = retry_scanners, []

    return len(mapp)

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    scanners, scanner = [], []
    for line in (r.strip() for r in raw.split('\n')):
        if line and line.startswith('--- scanner '):
            if scanner:
                scanners.append(scanner)
            scanner = []
        elif line:
            scanner.append(tuple(map(int, line.split(','))))
    scanners.append(scanner)
    return np.array(scanners, dtype=object)

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
