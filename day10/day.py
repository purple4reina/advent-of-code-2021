class Bracket(str):

    open_paren = '('
    open_brack = '['
    open_curly = '{'
    open_angle = '<'
    open_brackets = [open_paren, open_brack, open_curly, open_angle]

    close_paren = ')'
    close_brack = ']'
    close_curly = '}'
    close_angle = '>'
    close_brackets = [close_paren, close_brack, close_curly, close_angle]

    _points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    def is_open_brack(self):
        return self in self.open_brackets

    def is_valid_closer(self, closer):
        if self == self.open_paren:
            return closer == self.close_paren
        if self == self.open_brack:
            return closer == self.close_brack
        if self == self.open_curly:
            return closer == self.close_curly
        if self == self.open_angle:
            return closer == self.close_angle
        return False

    def points(self):
        return self._points[self]

def part1(inputs):

    def evaluate_system(line):
        root = Bracket('')
        system = root
        for char in line:
            bracket = Bracket(char)
            if bracket.is_open_brack():
                bracket.parent = system
                system = bracket
            elif system.is_valid_closer(bracket):
                system = system.parent
            else:
                return bracket.points()
        return 0

    points = 0
    for line in inputs:
        points += evaluate_system(line)

    return points

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    return raw.split()

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
