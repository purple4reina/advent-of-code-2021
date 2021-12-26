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

    _complete = (('A',)*2, ('B',)*2, ('C',)*2, ('D',)*2, (0,)*7)
    def complete(rooms):
        return rooms == _complete

    def move(rooms, start, stop):
        (i, j), (k, l) = start, stop
        new_rooms = [list(r) for r in rooms]
        new_rooms[i][j], new_rooms[k][l] = 0, new_rooms[i][j]
        return tuple(tuple(r) for r in new_rooms)

    def empty(rooms):
        return not any(rooms)

    def full(rooms, letter):
        return all(r == letter for r in rooms)

    _costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    _rooms = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    def movements(rooms):

        """
        #############
        #01.2.3.4.56#
        ###A#C#E#G###
          #B#D#F#H#
          #########
        """

        hall = rooms[4]

        # rooms
        for i, room in enumerate(rooms[:4]):
            for j, who in enumerate(room):
                if not who:
                    continue
                if all(a == _rooms[i] for a in rooms[i][j:]):
                    continue

                cost = _costs[who]
                if i == 0:
                    if not hall[1] and not hall[0]:
                        # A,0
                        # B,0
                        yield (i, j), (4, 0), cost * (3 + j)
                    if not hall[1]:
                        # A,1
                        # B,1
                        yield (i, j), (4, 1), cost * (2 + j)
                    if not hall[2]:
                        # A,2
                        # B,2
                        yield (i, j), (4, 2), cost * (2 + j)
                    if not hall[2] and not hall[3]:
                        # A,3
                        # B,3
                        yield (i, j), (4, 3), cost * (4 + j)
                    if not hall[2] and not hall[3] and not hall[4]:
                        # A,4
                        # B,4
                        yield (i, j), (4, 4), cost * (6 + j)
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not hall[5]:
                        # A,5
                        # B,5
                        yield (i, j), (4, 5), cost * (8 + j)
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not hall[5] and not hall[6]:
                        # A,6
                        # B,6
                        yield (i, j), (4, 6), cost * (9 + j)
                    if not hall[2] and not rooms[1][0] and \
                            rooms[1][1] == 'B' and who == 'B':
                        # A,C
                        # B,C
                        yield (i, j), (1, 0), cost * (4 + j)
                    if not hall[2] and not rooms[1][0] and who == 'B':
                        # A,D
                        # B,D
                        yield (i, j), (1, 1), cost * (5 + j)
                    if not hall[2] and not hall[3] and not rooms[2][0] and \
                            rooms[2][1] == 'C' and who == 'C':
                        # A,E
                        # B,E
                        yield (i, j), (2, 0), cost * (6 + j)
                    if not hall[2] and not hall[3] and not rooms[2][0] and \
                            who == 'C':
                        # A,F
                        # B,F
                        yield (i, j), (2, 1), cost * (7 + j)
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not rooms[3][0] and rooms[3][1] == 'D' and who == 'D':
                        # A,G
                        # B,G
                        yield (i, j), (3, 0), cost * (8 + j)
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not rooms[3][0] and who == 'D':
                        # A,H
                        # B,H
                        yield (i, j), (3, 1), cost * (9 + j)

                if i == 1:
                    if not hall[0] and not hall[1] and not hall[2]:
                        # C,0
                        # D,0
                        yield (i, j), (4, 0), cost * (5 + j)
                    if not hall[1] and not hall[2]:
                        # C,1
                        # D,1
                        yield (i, j), (4, 1), cost * (4 + j)
                    if not hall[2]:
                        # C,2
                        # D,2
                        yield (i, j), (4, 2), cost * (2 + j)
                    if not hall[3]:
                        # C,3
                        # D,3
                        yield (i, j), (4, 3), cost * (2 + j)
                    if not hall[3] and not hall[4]:
                        # C,4
                        # D,4
                        yield (i, j), (4, 4), cost * (4 + j)
                    if not hall[3] and not hall[4] and not hall[5]:
                        # C,5
                        # D,5
                        yield (i, j), (4, 5), cost * (6 + j)
                    if not hall[3] and not hall[4] and not hall[5] and \
                            not hall[6]:
                        # C,6
                        # D,6
                        yield (i, j), (4, 6), cost * (7 + j)
                    if not hall[2] and not rooms[0][0] and \
                            rooms[0][1] == 'A' and who == 'A':
                        # C,A
                        # D,A
                        yield (i, j), (0, 0), cost * (4 + j)
                    if not hall[2] and not rooms[0][0] and \
                            not rooms[0][1] and who == 'A':
                        # C,B
                        # D,B
                        yield (i, j), (0, 1), cost * (5 + j)
                    if not hall[3] and not rooms[2][0] and \
                            rooms[2][1] == 'C' and who == 'C':
                        # C,E
                        # D,E
                        yield (i, j), (2, 0), cost * (4 + j)
                    if not hall[3] and not rooms[2][0] and \
                            not rooms[2][1] and who == 'C':
                        # C,F
                        # D,F
                        yield (i, j), (2, 1), cost * (5 + j)
                    if not hall[3] and not hall[4] and not rooms[3][0] and \
                            rooms[3][1] == 'D' and who == 'D':
                        # C,G
                        # D,G
                        yield (i, j), (3, 0), cost * (6 + j)
                    if not hall[3] and not hall[4] and not rooms[3][0] and \
                            not rooms[3][1] and who == 'D':
                        # C,H
                        # D,H
                        yield (i, j), (3, 1), cost * (7 + j)

                if i == 2:
                    if not hall[0] and not hall[1] and not hall[2] and \
                            not hall[3]:
                        # E,0
                        # F,0
                        yield (i, j), (4, 0), cost * (7 + j)
                    if not hall[1] and not hall[2] and not hall[3]:
                        # E,1
                        # F,1
                        yield (i, j), (4, 1), cost * (6 + j)
                    if not hall[3] and not hall[2]:
                        # E,2
                        # F,2
                        yield (i, j), (4, 2), cost * (4 + j)
                    if not hall[3]:
                        # E,3
                        # F,3
                        yield (i, j), (4, 3), cost * (2 + j)
                    if not hall[4]:
                        # E,4
                        # F,4
                        yield (i, j), (4, 4), cost * (2 + j)
                    if not hall[4] and not hall[5]:
                        # E,5
                        # F,5
                        yield (i, j), (4, 5), cost * (4 + j)
                    if not hall[4] and not hall[5] and not hall[6]:
                        # E,6
                        # F,6
                        yield (i, j), (4, 6), cost * (5 + j)
                    if not hall[2] and not hall[3] and rooms[0][1] == 'A' and \
                            who == 'A':
                        # E,A
                        # F,A
                        yield (i, j), (0, 0), cost * (6 + j)
                    if not hall[2] and not hall[3] and not rooms[0][0] and \
                            who == 'A':
                        # E,B
                        # F,B
                        yield (i, j), (0, 1), cost * (7 + j)
                    if not hall[3] and not rooms[1][0] and \
                            rooms[1][1] == 'B' and who == 'B':
                        # E,C
                        # F,C
                        yield (i, j), (1, 0), cost * (4 + j)
                    if not hall[3] and not rooms[1][0] and \
                            not rooms[1][1] and who == 'B':
                        # E,D
                        # F,D
                        yield (i, j), (1, 1), cost * (4 + j)
                    if not hall[4] and not rooms[3][0] and \
                            rooms[3][1] == 'D' and who == 'D':
                        # E,G
                        # F,G
                        yield (i, j), (3, 0), cost * (4 + j)
                    if not hall[4] and not rooms[3][0] and \
                            not rooms[3][1] and who == 'D':
                        # E,H
                        # F,H
                        yield (i, j), (3, 1), cost * (5 + j)

                if i == 3:
                    if not hall[0] and not hall[1] and not hall[2] and \
                            not hall[3] and not hall[4]:
                        # G,0
                        # H,0
                        yield (i, j), (4, 0), cost * (9 + j)
                    if not hall[1] and not hall[2] and not hall[3] and \
                            not hall[4]:
                        # G,1
                        # H,1
                        yield (i, j), (4, 1), cost * (8 + j)
                    if not hall[2] and not hall[3] and not hall[4]:
                        # G,2
                        # H,2
                        yield (i, j), (4, 2), cost * (6 + j)
                    if not hall[3] and not hall[4]:
                        # G,3
                        # H,3
                        yield (i, j), (4, 3), cost * (4 + j)
                    if not hall[4]:
                        # G,4
                        # H,4
                        yield (i, j), (4, 4), cost * (2 + j)
                    if not hall[5]:
                        # G,5
                        # H,5
                        yield (i, j), (4, 5), cost * (2 + j)
                    if not hall[5] and not hall[6]:
                        # G,6
                        # H,6
                        yield (i, j), (4, 6), cost * (3 + j)
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not rooms[0][0] and rooms[0][1] == 'A' and who == 'A':
                        # G,A
                        # H,A
                        yield (i, j), (0, 0), cost * (8 + j)
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not rooms[0][0] and not rooms[0][1] and who == 'A':
                        # G,B
                        # H,B
                        yield (i, j), (0, 1), cost * (9 + j)
                    if not hall[3] and not hall[4] and not rooms[1][0] and \
                            rooms[1][1] == 'B' and who == 'B':
                        # G,C
                        # H,C
                        yield (i, j), (1, 0), cost * (6 + j)
                    if not hall[3] and not hall[4] and not rooms[1][0] and \
                            not rooms[1][1] and who == 'B':
                        # G,D
                        # H,D
                        yield (i, j), (1, 1), cost * (7 + j)
                    if not hall[4] and not rooms[2][0] and \
                            rooms[2][1] == 'C' and who == 'C':
                        # G,E
                        # H,E
                        yield (i, j), (2, 0), cost * (4 + j)
                    if not hall[4] and not rooms[2][0] and \
                            not rooms[2][1] and who == 'C':
                        # G,F
                        # H,F
                        yield (i, j), (2, 1), cost * (5 + j)

                break

        # hall
        for j, who in enumerate(hall):
            for k in range(2):
                if not who:
                    continue

                cost = _costs[who]
                if j == 0:
                    if not hall[1] and empty(rooms[0][:k+1]) and \
                            full(rooms[0][k+1:], 'A') and who == 'A':
                        # 0,A
                        # 0,B
                        yield (4, j), (0, k), cost * (3 + k)
                    if not hall[1] and not hall[2] and \
                            empty(rooms[1][:k+1]) and \
                            full(rooms[1][k+1:], 'B') and who == 'B':
                        # 0,C
                        # 0,D
                        yield (4, j), (1, k), cost * (5 + k)
                    if not hall[1] and not hall[2] and not hall[3] and \
                            empty(rooms[2][:k+1]) and \
                            full(rooms[2][k+1:], 'C') and who == 'C':
                        # 0,E
                        yield (4, j), (2, k), cost * (7 + k)
                    if not hall[1] and not hall[2] and not hall[3] and \
                            not hall[4] and empty(rooms[3][:k+1]) and \
                            full(rooms[3][k+1:], 'D') and who == 'D':
                        # 0,G
                        # 0,H
                        yield (4, j), (3, k), cost * (9 + k)

                if j == 1:
                    if empty(rooms[0][:k+1]) and \
                            full(rooms[0][k+1:], 'A') and who == 'A':
                        # 1,A
                        # 1,B
                        yield (4, j), (0, k), cost * (2 + k)
                    if not hall[2] and empty(rooms[1][:k+1]) and \
                            full(rooms[1][k+1:], 'B') and who == 'B':
                        # 1,C
                        # 1,D
                        yield (4, j), (1, k), cost * (4 + k)
                    if not hall[2] and not hall[3] and \
                            empty(rooms[2][:k+1]) and \
                            full(rooms[2][k+1:], 'C') and who == 'C':
                        # 1,E
                        yield (4, j), (2, k), cost * (6 + k)
                    if not hall[2] and not hall[3] and not hall[4] and \
                            empty(rooms[3][:k+1]) and \
                            full(rooms[3][k+1:], 'D') and who == 'D':
                        # 1,G
                        # 1,H
                        yield (4, j), (3, k), cost * 8

                if j == 2:
                    if empty(rooms[0][:k+1]) and \
                            full(rooms[0][k+1:], 'A') and who == 'A':
                        # 2,A
                        # 2,B
                        yield (4, j), (0, k), cost * (2 + k)
                    if empty(rooms[1][:k+1]) and \
                            full(rooms[1][k+1:], 'B') and who == 'B':
                        # 2,C
                        # 2,D
                        yield (4, j), (1, k), cost * (2 + k)
                    if not hall[3] and empty(rooms[2][:k+1]) and \
                            full(rooms[2][k+1:], 'C') and who == 'C':
                        # 2,E
                        # 2,F
                        yield (4, j), (2, k), cost * (4 + k)
                    if not hall[3] and not hall[4] and \
                            empty(rooms[3][:k+1]) and \
                            full(rooms[3][k+1:], 'D') and who == 'D':
                        # 2,G
                        # 2,H
                        yield (4, j), (3, k), cost * (6 + k)

                if j == 3:
                    if not hall[2] and not rooms[0][0] and rooms[0][1] == 'A' and \
                            who == 'A':
                        # 3,A
                        yield (4, j), (0, 0), cost * 4
                    if not hall[2] and not rooms[0][0] and not rooms[0][1] and \
                            who == 'A':
                        # 3,B
                        yield (4, j), (0, 1), cost * 5
                    if not rooms[1][0] and rooms[1][1] == 'B' and who == 'B':
                        # 3,C
                        yield (4, j), (1, 0), cost * 2
                    if not rooms[1][0] and not rooms[1][1] and who == 'B':
                        # 3,D
                        yield (4, j), (1, 1), cost * 3
                    if not rooms[2][0] and rooms[2][1] == 'C' and who == 'C':
                        # 3,E
                        yield (4, j), (2, 0), cost * 2
                    if not rooms[2][0] and not rooms[2][1] and who == 'C':
                        # 3,F
                        yield (4, j), (2, 1), cost * 3
                    if not hall[4] and not rooms[3][0] and rooms[3][1] == 'D' and \
                            who == 'D':
                        # 3,G
                        yield (4, j), (3, 0), cost * 4
                    if not hall[4] and not rooms[3][0] and not rooms[3][1] and \
                            who == 'D':
                        # 3,H
                        yield (4, j), (3, 1), cost * 5

                if j == 4:
                    if not hall[2] and not hall[3] and not rooms[0][0] and \
                            rooms[0][1] == 'A' and who == 'A':
                        # 4,A
                        yield (4, j), (0, 0), cost * 6
                    if not hall[2] and not hall[3] and not rooms[0][0] and \
                            not rooms[0][1] and who == 'A':
                        # 4,B
                        yield (4, j), (0, 1), cost * 7
                    if not hall[3] and not rooms[1][0] and rooms[1][1] == 'B' and \
                            who == 'B':
                        # 4,C
                        yield (4, j), (1, 0), cost * 4
                    if not hall[3] and not rooms[1][0] and not rooms[1][1] and \
                            who == 'B':
                        # 4,D
                        yield (4, j), (1, 1), cost * 5
                    if not rooms[2][0] and rooms[2][1] == 'C' and who == 'C':
                        # 4,E
                        yield (4, j), (2, 0), cost * 2
                    if not rooms[2][0] and not rooms[2][1] and who == 'C':
                        # 4,F
                        yield (4, j), (2, 1), cost * 3
                    if not rooms[3][0] and rooms[3][1] == 'D' and who == 'D':
                        # 4,G
                        yield (4, j), (3, 0), cost * 2
                    if not rooms[3][0] and not rooms[3][1] and who == 'D':
                        # 4,H
                        yield (4, j), (3, 1), cost * 3

                if j == 5:
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not rooms[0][0] and rooms[0][1] == 'A' and who == 'A':
                        # 5,A
                        yield (4, j), (0, 0), cost * 8
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not rooms[0][0] and not rooms[0][1] and who == 'A':
                        # 5,B
                        yield (4, j), (0, 1), cost * 9
                    if not hall[3] and not hall[4] and not rooms[1][0] and \
                            rooms[1][1] == 'B' and who == 'B':
                        # 5,C
                        yield (4, j), (1, 0), cost * 6
                    if not hall[3] and not hall[4] and not rooms[1][0] and \
                            not rooms[1][1] and who == 'B':
                        # 5,D
                        yield (4, j), (1, 1), cost * 7
                    if not hall[4] and not rooms[2][0] and rooms[2][1] == 'C' and \
                            who == 'C':
                        # 5,E
                        yield (4, j), (2, 0), cost * 4
                    if not hall[4] and not rooms[2][0] and not rooms[2][1] and \
                            who == 'C':
                        # 5,F
                        yield (4, j), (2, 1), cost * 5
                    if not rooms[3][0] and rooms[3][1] == 'D' and who == 'D':
                        # 5,G
                        yield (4, j), (3, 0), cost * 2
                    if not rooms[3][0] and not rooms[3][1] and who == 'D':
                        # 5,H
                        yield (4, j), (3, 1), cost * 3

                if j == 6:
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not hall[5] and not rooms[0][0] and \
                            rooms[0][1] == 'A' and who == 'A':
                        # 6,A
                        yield (4, j), (0, 0), cost * 9
                    if not hall[2] and not hall[3] and not hall[4] and \
                            not hall[5] and not rooms[0][0] and \
                            not rooms[0][1] and who == 'A':
                        # 6,B
                        yield (4, j), (0, 1), cost * 10
                    if not hall[3] and not hall[4] and not hall[5] and \
                            not rooms[1][0] and rooms[1][1] == 'B' and who == 'B':
                        # 6,C
                        yield (4, j), (1, 0), cost * 7
                    if not hall[3] and not hall[4] and not hall[5] and \
                            not rooms[1][0] and not rooms[1][1] and who == 'B':
                        # 6,D
                        yield (4, j), (1, 1), cost * 8
                    if not hall[4] and not hall[5] and not rooms[2][0] and \
                            rooms[2][1] == 'C' and who == 'C':
                        # 6,E
                        yield (4, j), (2, 0), cost * 5
                    if not hall[4] and not hall[5] and not rooms[2][0] and \
                            not rooms[2][1] and who == 'C':
                        # 6,F
                        yield (4, j), (2, 1), cost * 6
                    if not hall[5] and not rooms[3][0] and rooms[3][1] == 'D' and \
                            who == 'D':
                        # 6,G
                        yield (4, j), (3, 0), cost * 3
                    if not hall[5] and not rooms[3][0] and not rooms[3][1] and \
                            who == 'D':
                        # 6,H
                        yield (4, j), (3, 1), cost * 4

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
    shuffle(rooms, 0)
    return min_energy[0]

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
