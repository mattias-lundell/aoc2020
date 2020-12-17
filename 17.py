from collections import Counter
from itertools import chain


def part1(data):
    grid = set()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                grid.add((x, y, 0))

    for i in range(6):
        counts = Counter(chain.from_iterable(neighbours_3d(p) for p in grid))
        grid = {
            k
            for k, v in counts.items() if v == 3 or (k in grid and v == 2)
        }

    return len(grid)


def part2(data):
    grid = set()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                grid.add((x, y, 0, 0))

    for i in range(6):
        counts = Counter(chain.from_iterable(neighbours_4d(p) for p in grid))
        grid = {
            k
            for k, v in counts.items() if v == 3 or (k in grid and v == 2)
        }

    return len(grid)


def neighbours_3d(p):
    (x0, y0, z0) = p
    res = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if [dx, dy, dz] != [0, 0, 0]:
                    res.append((x0 + dx, y0 + dy, z0 + dz))
    return res


def neighbours_4d(p):
    (x0, y0, z0, w0) = p
    res = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if [dx, dy, dz, dw] != [0, 0, 0, 0]:
                        res.append((x0 + dx, y0 + dy, z0 + dz, w0 + dw))
    return res
