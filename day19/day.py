import itertools
import numpy as np

def _rotations_2():
    R2_0 = np.array([[1, 0], [0, 1]])
    R2_1 = np.array([[0, 1], [-1, 0]])
    R2_2 = R2_1 @ R2_1
    R2_3 = R2_2 @ R2_1
    return [R2_0, R2_1, R2_2, R2_3]

def _rotations_3():
    rots = []
    for x, y, z in itertools.permutations([0, 1, 2]):
        for sx, sy, sz in itertools.product([-1, 1], repeat=3):
            rotation_matrix = np.zeros((3, 3))
            rotation_matrix[0, x] = sx
            rotation_matrix[1, y] = sy
            rotation_matrix[2, z] = sz
            if np.linalg.det(rotation_matrix) == 1:
                rots.append(rotation_matrix)
    return rots

_rotations = {2: _rotations_2(), 3: _rotations_3()}

def part1(scanners, overlap=12):

    mapp = {tuple(s): True for s in scanners[0]}
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
                    mapp[tuple(r + max_distance)] = True
                break

            else:
                retry_scanners.append(scanner)
        scanners, retry_scanners = retry_scanners, []

    return len(mapp)

def part2(scanners, overlap=12):

    mapp = {tuple(s): True for s in scanners[0]}
    dims = len(scanners[0][0])
    scanners, retry_scanners = [np.array(s) for s in scanners[1:]], []
    scanner_locations = []

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
                    mapp[tuple(r + max_distance)] = True

                scanner_locations.append(max_distance)
                break

            else:
                retry_scanners.append(scanner)
        scanners, retry_scanners = retry_scanners, []

    manhatan_max = 0
    for scanner1 in scanner_locations:
        for scanner2 in scanner_locations:
            dist = sum(abs(v1 - v2) for v1, v2 in zip(scanner1, scanner2))
            if dist > manhatan_max:
                manhatan_max = dist

    return int(manhatan_max)

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
