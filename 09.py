from itertools import combinations
from helpers import ints


def part1(data):
    return find(ints(data))


def find(data):
    x = 5 if len(data) < 100 else 25
    for i in range(x, len(data)):
        sums = set([a + b for (a, b) in combinations(data[i - x:i], 2)])
        if data[i] not in sums:
            return data[i]


def part2(data):
    data = ints(data)
    hit = find(data)

    for n in range(2, len(data)):
        for i in range(len(data), 0, -1):
            subset = data[i - n:i]
            if sum(subset) == hit:
                return (max(subset) + min(subset))
