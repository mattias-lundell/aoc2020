from math import prod


def part1(data):
    return solve(data, 3, 1)


def part2(data):
    return prod([
        solve(data, dx, dy)
        for (dx, dy) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    ])


def solve(data, dx, dy):
    repeats = len(data) + 1

    grid = []
    for row in data:
        grid.append(repeats * row.strip())

    x = 0
    y = 0
    cnt = 0
    while True:
        if grid[y][x] == '#':
            cnt += 1
        x += dx
        y += dy

        if y >= len(grid):
            break

    return (cnt)
