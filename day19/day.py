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
        rotated_scanner = []
        for vector in scanner:
            rotated_scanner.append(tuple(rotation @ vector))
        yield rotated_scanner

def add_to_axis(vectors, offset, axis=0):
    new_vectors = []
    for vector in vectors:
        new_vector = vector[:axis] + (vector[axis] + offset,) + vector[axis+1:]
        new_vectors.append(new_vector)
    return new_vectors

def place_scan(mapp, scanner, overlap=12):
    dims = len(scanner[0])
    start = min(min(point) for point in mapp) - 1000
    end = max(max(point) for point in mapp) + 1000
    for rotation in rotations(scanner, dims=dims):
        for location in itertools.product(range(start, end+1), repeat=dims):
            rotated_offset = rotation
            for axis, offset in enumerate(location):
                rotated_offset = add_to_axis(rotated_offset, offset, axis=axis)
            rotated_and_offset_set = set(tuple(r) for r in rotated_offset)
            if len(mapp & rotated_and_offset_set) >= overlap:
                mapp |= rotated_and_offset_set
                return mapp, True
    return mapp, False

def part1(scanners, overlap=12):
    mapp, scanners = set(tuple(s) for s in scanners[-1]), scanners[:-1]
    while scanners.any():
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
