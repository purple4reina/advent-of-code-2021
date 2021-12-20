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

def part1(scanners, overlap=12):

    mapp = set(scanners[0])
    scanners = [np.array(s) for s in scanners[1:]]
    dims = len(scanners[0][0])

    while len(scanners):
        retry_scanners = []
        for scanner in scanners:
            for rotation in ((r @ scanner.T).T for r in _rotations[dims]):

                distances = {}
                for a1 in mapp:
                    for a2 in rotation:
                        dist = sum(v1 - v2 for v1, v2 in zip(a1, a2))
                        distances[dist] = distances.get(dist, 0) + 1

                max_count, max_distance = max((v,k) for k,v in distances.items())
                if max_count < overlap:
                    continue

                for axis, distance in enumerate(max_distance):
                    rotation[:,axis] += distance
                for r in rotation:
                    mapp.add(tuple(r))
                break

            else:
                retry_scanners.append(scanner)

        scanners = retry_scanners

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
