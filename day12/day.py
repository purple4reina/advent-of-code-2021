def part1(cave_map):

    def paths(loc_from, visited):
        if loc_from == 'end':
            return 1
        count = 0
        for loc_to in cave_map[loc_from]:
            if loc_to.islower() and (loc_to in visited) and loc_to != 'end':
                continue
            new_visted = visited.copy()
            new_visted[loc_to] = True
            count += paths(loc_to, new_visted)
        return count

    return paths('start', {'start': True})

def part2(cave_map):

    def paths(loc_from, visited):
        if loc_from == 'end':
            return 1
        count = 0
        for loc_to in cave_map[loc_from]:
            loc_stat = visited.get(loc_to, 0)
            new_visted = visited.copy()
            if loc_to.islower():
                if loc_stat == 2:
                    continue
                if loc_stat == 1 and 2 in visited.values():
                    continue
                if loc_to == 'start':
                    continue
                new_visted[loc_to] = loc_stat + 1
            count += paths(loc_to, new_visted)
        return count

    return paths('start', {'start': 1})

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    cave_map = {}
    for conn in raw.split():
        a, b = conn.split('-')
        cave_map.setdefault(a, []).append(b)
        cave_map.setdefault(b, []).append(a)
    return cave_map

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
