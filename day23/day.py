def memoize(fn):
    _cache = {}
    def wrap(*args):
        if args in _cache:
            return _cache[args]
        ret = fn(*args)
        _cache[args] = ret
        return ret
    return wrap

def part1(rooms):
    print('rooms: ', rooms)

    def complete(rooms):
        return rooms[0][0] == 'A' and rooms[0][1] == 'A' and \
                rooms[1][0] == 'B' and rooms[1][1] == 'B' and \
                rooms[2][0] == 'C' and rooms[2][1] == 'C' and \
                rooms[3][0] == 'D' and rooms[3][1] == 'D'

    def move(rooms, start, stop):
        (i, j), (k, l) = start, stop
        new_rooms = [list(r) for r in rooms]
        new_rooms[i][j], new_rooms[k][l] = 0, new_rooms[i][j]
        return tuple(tuple(r) for r in new_rooms)

    _costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    def movements(rooms):
        hall = rooms[4]

        # rooms
        for i, room in enumerate(rooms[:4]):
            for j, who in enumerate(room):
                if not who:
                    continue
                cost = _costs[who]
                if i == 0:
                    if who == 'A':
                        continue
                    if not hall[1]:
                        # A,1
                        # B,1
                        yield (i, j), (4, 1), cost * (2 + j)
                        if not hall[0]:
                            # A,0
                            # B,0
                            yield (i, j), (4, 0), cost * (3 + j)
                    if not hall[2]:
                        # A,2
                        # B,2
                        yield (i, j), (4, 2), cost * (2 + j)
                        if who == 'B':
                            if not rooms[1][0]:
                                if rooms[1][1] == 'B':
                                    # A,C
                                    # B,C
                                    yield (i, j), (1, 0), cost * (4 + j)
                                if not rooms[1][1]:
                                    # A,D
                                    # B,D
                                    yield (i, j), (1, 1), cost * (5 + j)
                        if not hall[3]:
                            # A,3
                            # B,3
                            yield (i, j), (4, 3), cost * (4 + j)
                            if who == 'C':
                                if not rooms[2][0]:
                                    if rooms[2][1] == 'C':
                                        # A,E
                                        # B,E
                                        yield (i, j), (2, 0), cost * (6 + j)
                                    if not rooms[2][1]:
                                        # A,F
                                        # B,F
                                        yield (i, j), (2, 1), cost * (7 + j)
                            if not hall[4]:
                                # A,4
                                # B,4
                                yield (i, j), (4, 4), cost * (6 + j)
                                if who == 'D':
                                    if not rooms[3][0]:
                                        if rooms[3][1] == 'D':
                                            # A,G
                                            # B,G
                                            yield (i, j), (3, 0), cost * (8 + j)
                                        if not rooms[2][1]:
                                            # A,H
                                            # B,H
                                            yield (i, j), (3, 1), cost * (9 + j)
                                if not hall[5]:
                                    # A,5
                                    # B,5
                                    yield (i, j), (4, 5), cost * (8 + j)
                                    if not hall[6]:
                                        # A,6
                                        # B,6
                                        yield (i, j), (4, 6), cost * (9 + j)

        """
        #############
        #01.2.3.4.56#
        ###A#C#E#G###
          #B#D#F#H#
          #########
        """
                if i == 1:
                    if who == 'B':
                        continue
                    if not hall[2]:
                        yield (i, j), (4, 2), cost * (2 + j)
                        if who == 'A':
                            if not rooms[1][0]:
                                if rooms[1][1] == 'B':
                                    yield (i, j), (1, 0), cost * (4 + j)
                                if not rooms[1][1]:
                                    yield (i, j), (1, 1), cost * (5 + j)
                        if not hall[1]:
                            yield (i, j), (4, 1), cost * (2 + j)
                            if not hall[0]:
                                yield (i, j), (4, 0), cost * (3 + j)
                        if not hall[3]:
                            yield (i, j), (4, 3), cost * (4 + j)
                            if who == 'C':
                                if not rooms[2][0]:
                                    if rooms[2][1] == 'C':
                                        yield (i, j), (2, 0), cost * (6 + j)
                                    if not rooms[2][1]:
                                        yield (i, j), (2, 1), cost * (7 + j)
                            if not hall[4]:
                                yield (i, j), (4, 4), cost * (6 + j)
                                if who == 'D':
                                    if not rooms[3][0]:
                                        if rooms[3][1] == 'D':
                                            yield (i, j), (3, 0), cost * (8 + j)
                                        if not rooms[2][1]:
                                            yield (i, j), (3, 1), cost * (9 + j)
                                if not hall[5]:
                                    yield (i, j), (4, 5), cost * (8 + j)
                                    if not hall[6]:
                                        yield (i, j), (4, 6), cost * (9 + j)

                break
        # C,0
        # C,1
        # C,2
        # C,3
        # C,4
        # C,5
        # C,6
        # C,A
        # C,B
        # C,E
        # C,F
        # C,G
        # C,H

        # D,0
        # D,1
        # D,2
        # D,3
        # D,4
        # D,5
        # D,6
        # D,A
        # D,B
        # D,E
        # D,F
        # D,G
        # D,H

        # E,0
        # E,1
        # E,2
        # E,3
        # E,4
        # E,5
        # E,6
        # E,A
        # E,B
        # E,C
        # E,D
        # E,G
        # E,H

        # F,0
        # F,1
        # F,2
        # F,3
        # F,4
        # F,5
        # F,6
        # F,A
        # F,B
        # F,C
        # F,D
        # F,G
        # F,H

        # G,0
        # G,1
        # G,2
        # G,3
        # G,4
        # G,5
        # G,6
        # G,A
        # G,B
        # G,C
        # G,D
        # G,E
        # G,F

        # H,0
        # H,1
        # H,2
        # H,3
        # H,4
        # H,5
        # H,6
        # H,A
        # H,B
        # H,C
        # H,D
        # H,E
        # H,F

        # hall
        for j, who in enumerate(hall):
            if not who:
                continue


        # 0,A
        # 0,B
        # 0,C
        # 0,D
        # 0,E
        # 0,F
        # 0,G
        # 0,H

        # 1,A
        # 1,B
        # 1,C
        # 1,D
        # 1,E
        # 1,F
        # 1,G
        # 1,H

        # 2,A
        # 2,B
        # 2,C
        # 2,D
        # 2,E
        # 2,F
        # 2,G
        # 2,H

        # 3,A
        # 3,B
        # 3,C
        # 3,D
        # 3,E
        # 3,F
        # 3,G
        # 3,H

        # 4,A
        # 4,B
        # 4,C
        # 4,D
        # 4,E
        # 4,F
        # 4,G
        # 4,H

        # 5,A
        # 5,B
        # 5,C
        # 5,D
        # 5,E
        # 5,F
        # 5,G
        # 5,H

        # 6,A
        # 6,B
        # 6,C
        # 6,D
        # 6,E
        # 6,F
        # 6,G
        # 6,H

    @memoize
    def shuffle(rooms, energy):
        if energy > min_energy[0]:
            return
        if complete(rooms):
            min_energy[0] = min(min_energy[0], energy)
            return
        for start, stop, cost in movements(rooms):
            shuffle(move(rooms, start, stop), energy + cost)

    min_energy = [float('inf')]
    return shuffle(rooms, 0)

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    rooms = [[] for _ in range(4)]
    for line in raw.split():
        line = line.strip('#').strip('.')
        if not line:
            continue
        bugs = line.split('#')
        for i, b in enumerate(bugs):
            rooms[i].append(b)
    return (tuple(rooms[0]), tuple(rooms[1]), tuple(rooms[2]), tuple(rooms[3]),
            tuple([0] * 7))

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
