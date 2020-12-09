from itertools import combinations


def part1(data):
    x = 5 if len(data) < 100 else 25
    for i in range(x, len(data)):
        prev = data[i - x:i]
        curr = int(data[i])
        sums = set([int(a) + int(b) for (a, b) in combinations(prev, 2)])

        if curr not in sums:
            return curr


def find(data):
    x = 5 if len(data) < 100 else 25
    for i in range(x, len(data)):
        prev = data[i - x:i]
        curr = int(data[i])
        sums = set([int(a) + int(b) for (a, b) in combinations(prev, 2)])

        if curr not in sums:
            return curr


def part2(data):
    hit = find(data)

    data = [int(x) for x in data]

    for n in range(2, len(data)):
        for i in range(len(data), 0, -1):
            subset = data[i - n:i]
            if sum(subset) == hit:
                return (max(subset) + min(subset))
