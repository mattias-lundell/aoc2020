import itertools
from collections import Counter
from functools import lru_cache


class Cube:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def coordinates(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __hash__(self):
        return hash(self.coordinates)

    def e(self):
        self.x += 1
        self.y -= 1
        return self

    def se(self):
        self.y -= 1
        self.z += 1
        return self

    def sw(self):
        self.x -= 1
        self.z += 1
        return self

    def w(self):
        self.x -= 1
        self.y += 1
        return self

    def nw(self):
        self.y += 1
        self.z -= 1
        return self

    def ne(self):
        self.x += 1
        self.z -= 1
        return self

    @property
    @lru_cache(maxsize=None)
    def neighbours(self):
        return [
            Cube(self.x + 1, self.y - 1, self.z),
            Cube(self.x + 1, self.y, self.z - 1),
            Cube(self.x, self.y + 1, self.z - 1),
            Cube(self.x - 1, self.y + 1, self.z),
            Cube(self.x - 1, self.y, self.z + 1),
            Cube(self.x, self.y - 1, self.z + 1),
        ]

    def move(self, steps):
        for step in steps:
            {
                'e': self.e,
                'se': self.se,
                'sw': self.sw,
                'w': self.w,
                'nw': self.nw,
                'ne': self.ne,
            }[step]()


def parse_line(line):
    one_letters = set(['e', 'w'])
    two_letters = set(['se', 'sw', 'ne', 'nw'])

    res = []
    line = iter(line)
    try:
        while True:
            c = next(line)
            if c in set(['s', 'n']):
                cc = next(line)
                res.append(''.join([c, cc]))
            else:
                res.append(c)
    except StopIteration:
        pass

    return res


def part1(data):
    black = set()
    for line in data:
        c = Cube()
        c.move(parse_line(line))
        if c in black:
            black.discard(c)
        else:
            black.add(c)

    return len(black)


def part2(data):
    black = set()
    for line in data:
        c = Cube()
        c.move(parse_line(line))
        if c in black:
            black.discard(c)
        else:
            black.add(c)

    for _ in range(100):
        new_black = set()

        for c in black:
            cnt = len([n for n in c.neighbours if n in black])
            if cnt == 1 or cnt == 2:
                new_black.add(c)

        white = set()
        for c in black:
            white.update([cc for cc in c.neighbours])
        white -= black

        for c in white:
            cnt = len([n for n in c.neighbours if n in black])
            if cnt == 2:
                new_black.add(c)

        black = new_black

    return len(black)
