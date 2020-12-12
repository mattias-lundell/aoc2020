import os


def part1(data):
    seats = [list(lines) for lines in data]

    cnt = 0
    while True:
        next_gen = step(seats)
        if next_gen == seats:
            return count_occupied(seats)
        seats = next_gen
        cnt += 1

    return cnt


def print_seats(seats):
    os.system('clear')
    for row in seats:
        print(''.join(row))
    print()


def step(seats):
    next_gen = [list(rows) for rows in seats]
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            cnt = count_occupied_adjacent(seats, row, col)
            seat = seats[row][col]
            if seat == 'L':
                if cnt == 0:
                    next_gen[row][col] = '#'
            elif seat == '#':
                if cnt >= 4:
                    next_gen[row][col] = 'L'
    return next_gen


def count_occupied(seats):
    cnt = 0
    for row in seats:
        for col in row:
            if col == '#':
                cnt += 1

    return cnt


from functools import lru_cache


@lru_cache(maxsize=None)
def neighbours(row, col, rows, cols, distance=1):
    res = []
    for [d_row, d_col] in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1)]:
        _row = row + d_row * distance
        _col = col + d_col * distance
        if _row < 0 or _row >= rows or _col < 0 or _col >= cols:
            continue
        res.append((_row, _col))
    return res


def count_occupied_adjacent(seats, row, col):
    cnt = 0

    rows = len(seats)
    cols = len(seats[0])

    for (_row, _col) in neighbours(row, col, rows, cols):
        if seats[_row][_col] == '#':
            cnt += 1
    return cnt


def part2(data):

    seats = {}

    for i, rows in enumerate(data):
        for j, c in enumerate(rows):
            if c in "#L":
                seats[(i, j)] = c

    rows = len(data)
    cols = len(data[0])

    cnt = 0
    while True:
        modified, next_gen = step2(seats, max(rows, cols), rows, cols)
        if not modified:
            return len([x for x in seats.values() if x == '#'])
        seats = next_gen
        cnt += 1


def step2(seats, ray_len, rows, cols):
    swaps = []
    modified = False
    for seat in seats:
        cnt = count_adjacent_part2(seats, seat, ray_len, rows, cols)
        _seat = seats[seat]
        if _seat == 'L' and cnt == 0:
            swaps.append(seat)
        elif _seat == '#' and cnt >= 5:
            swaps.append(seat)

    if len(swaps) > 0:
        modified = True
        for swap in swaps:
            seats[swap] = _swap[seats[swap]]

    return modified, seats


_swap = {
    '#': 'L',
    'L': '#',
}

_n2_cache = {}


def neighbours2(seats, seat, rows, cols, distance=100):
    if (seat, distance) in _n2_cache:
        return _n2_cache[(seat, distance)]

    res = []
    (row, col) = seat
    for [d_row, d_col] in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1)]:
        for d in range(1, distance + 1):
            _row = row + d_row * d
            _col = col + d_col * d
            if _row < 0 or _row >= rows or _col < 0 or _col >= cols:
                break
            elif (_row, _col) in seats:
                res.append((_row, _col))
                break

    _n2_cache[seat] = res
    return res


def count_adjacent_part2(seats, seat, n_max, rows, cols):
    return len([
        seat for seat in neighbours2(seats, seat, rows, cols)
        if seats[seat] == '#'
    ])
