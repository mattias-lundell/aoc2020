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

    def solve(adapters=[]):
        d = {0: 1}
        for adapter in adapters:
            d[adapter] = sum([
                d.get(adapter - 1, 0),
                d.get(adapter - 2, 0),
                d.get(adapter - 3, 0),
            ])

        return d[adapters[-1]]

    return solve(adapters)
