import itertools
import numpy as np

# 2-dimensions
R2_0 = np.array([[1, 0], [0, 1]])
R2_1 = np.array([[0, 1], [-1, 0]])
R2_2 = R2_1 @ R2_1
R2_3 = R2_2 @ R2_1

# 3-dimensions
_Rx = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
_Ry = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])
_Rz = np.array([[1, 0, 0], [-1, 0, 0], [0, 0, 1]])
_I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

R3_0  = _I
R3_1  = _I                                     @ _Rz
R3_2  = _I                                     @ _Rz @ _Rz
R3_3  = _I                                     @ _Rz @ _Rz @_Rz
R3_4  = _I @ _Rx
R3_5  = _I @ _Rx                               @ _Rz
R3_6  = _I @ _Rx                               @ _Rz @ _Rz
R3_7  = _I @ _Rx                               @ _Rz @ _Rz @ _Rz
R3_8  = _I @ _Rx @ _Rx
R3_9  = _I @ _Rx @ _Rx                         @ _Rz
R3_10  = _I @ _Rx @ _Rx                         @ _Rz @ _Rz
R3_11  = _I @ _Rx @ _Rx                         @ _Rz @ _Rz @ _Rz
R3_12  = _I @ _Rx @ _Rx @ _Rx
R3_13  = _I @ _Rx @ _Rx @ _Rx                   @ _Rz
R3_14  = _I @ _Rx @ _Rx @ _Rx                   @ _Rz @ _Rz
R3_15  = _I @ _Rx @ _Rx @ _Rx                   @ _Rz @ _Rz @ _Rz
R3_16  = _I                   @ _Ry
R3_17  = _I                   @ _Ry             @ _Rz
R3_18  = _I                   @ _Ry             @ _Rz @ _Rz
R3_19  = _I                   @ _Ry             @ _Rz @ _Rz @ _Rz
R3_20  = _I                   @ _Ry @ _Ry @ _Ry
R3_21  = _I                   @ _Ry @ _Ry @ _Ry @ _Rz
R3_22  = _I                   @ _Ry @ _Ry @ _Ry @ _Rz @ _Rz
R3_23  = _I                   @ _Ry @ _Ry @ _Ry @ _Rz @ _Rz @ _Rz

_rotations = {
        2: [R2_0, R2_1, R2_2, R2_3],
        3: [R3_0,  R3_1,  R3_2,  R3_3,  R3_4,  R3_5,  R3_6,  R3_7,
            R3_8,  R3_9,  R3_10, R3_11, R3_12, R3_13, R3_14, R3_15,
            R3_16, R3_17, R3_18, R3_19, R3_20, R3_21, R3_22, R3_23],
}

def rotations(scanner, dims=2):
    for rotation in _rotations[dims]:
        yield (rotation @ scanner.T).T

def calculate_distances(arr1, arr2):
    distances = {}
    for a1 in arr1:
        for a2 in arr2:
            dist = tuple(v1 - v2 for v1, v2 in zip(a1, a2))
            distances[dist] = distances.get(dist, 0) + 1
    return distances

def place_scan(mapp, scanner, overlap=12):
    dims = len(scanner[0])
    for rotation in rotations(scanner, dims=dims):
        all_distances = calculate_distances(mapp, rotation)
        max_count, max_distance = max((v,k) for k,v in all_distances.items())
        if max_count < overlap:
            continue
        for axis, distance in enumerate(max_distance):
            rotation[:,axis] += distance
        for r in rotation:
            mapp.add(tuple(r))
        return mapp, True
    return mapp, False

def part1(scanners, overlap=12):
    mapp = set(tuple(s) for s in scanners[-1])
    scanners = [np.array(s) for s in scanners[:-1]]
    while len(scanners):
        retry_scanners = []
        for scanner in scanners:
            mapp, placed = place_scan(mapp, scanner, overlap=overlap)
            if not placed:
                retry_scanners.append(scanner)
        scanners = np.array(retry_scanners)
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
