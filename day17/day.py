def part1(inputs):

    xmin, xmax, ymin, ymax = inputs

    def in_target(xloc, yloc):
        return xloc >= xmin and xloc <= xmax and \
                yloc >= ymin and yloc <= ymax

    def past_target(xloc, yloc):
        return xloc > xmax or yloc < ymin

    maxy = 0
    for x in range(10000):
        for y in range(10000):
            this_maxy = xloc = yloc = 0
            xvel, yvel = x, y
            while True:
                xloc += xvel
                yloc += yvel

                this_maxy = max(this_maxy, yloc)

                if xvel > 0:
                    xvel -= 1
                yvel -= 1

                if in_target(xloc, yloc):
                    maxy = max(maxy, this_maxy)
                    break
                if past_target(xloc, yloc):
                    break

    return maxy

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    raw = raw.lstrip('target area: ')
    xrange, yrange = raw.split(', ')
    xmin, xmax = map(int, xrange.lstrip('x=').split('..'))
    ymin, ymax = map(int, yrange.lstrip('y=').split('..'))
    return xmin, xmax, ymin, ymax

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
