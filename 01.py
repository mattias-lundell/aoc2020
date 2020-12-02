import itertools


def part1(data):
    data = sorted([int(x.strip()) for x in data if x])
    pairs = itertools.combinations(data, 2)

    for (a, b) in pairs:
        if a + b == 2020:
            return a * b


def part2(data):
    data = sorted([int(x.strip()) for x in data if x])
    pairs = itertools.combinations(data, 3)

    for (a, b, c) in pairs:
        if a + b + c == 2020:
            return a * b * c
