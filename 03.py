from math import prod


def part1(data):
    return solve(data, 3, 1)


def part2(data):
    return prod([
        solve(data, dx, dy)
        for (dx, dy) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    ])


def solve(data, dx, dy):
    x = y = cnt = 0
    while y < len(data):
        if data[y][x] == '#':
            cnt += 1
        y += dy
        x = (x + dx) % len(data[0])

    return (cnt)
