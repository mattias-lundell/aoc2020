from helpers import ints
from itertools import combinations


def part1(data):
    data = sorted(ints(data))

    curr = one = 0
    three = 1

    for d in data:
        diff = d - curr
        if diff == 1:
            one += 1
            curr += 1
        elif diff == 3:
            three += 1
            curr += 3
        else:
            raise Exception(d)

    return one * three


def part2(data):
    adapters = sorted(ints(data))
    cache = {}

    def solve(adapters=[], start=0, target=0):
        key = (len(adapters), start)
        if key in cache:
            return cache[key]

        if len(adapters) == 0:
            return 1 if target - start <= 3 else 0

        cnt = 0
        head = adapters[0]
        # include head
        if head - start <= 3:
            cnt = solve(adapters[1:], head, target)
        # ignore head
        cnt += solve(adapters[1:], start, target)

        cache[key] = cnt

        return cnt

    return solve(adapters, 0, max(adapters) + 3)
