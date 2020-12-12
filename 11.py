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


def count_occupied_adjacent(seats, row, col):
    rows = len(seats)
    cols = len(seats[0])
    cnt = 0
    for [d_row, d_col] in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1)]:
        _row = row + d_row
        _col = col + d_col
        if _row < 0 or _row >= rows or _col < 0 or _col >= cols:
            continue
        if seats[_row][_col] == '#':
            cnt += 1
    return cnt


def part2(data):
    seats = [list(lines) for lines in data]

    cnt = 0
    while True:
        next_gen = step2(seats, max(len(data), len(data[0])))
        if next_gen == seats:
            return count_occupied(seats)
        seats = next_gen
        cnt += 1


def step2(seats, ray_len):
    next_gen = [list(rows) for rows in seats]
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            cnt = count_adjacent_part2(seats, row, col, ray_len)
            if seats[row][col] == 'L':
                if cnt == 0:
                    next_gen[row][col] = '#'
            elif seats[row][col] == '#':
                if cnt >= 5:
                    next_gen[row][col] = 'L'
    return next_gen


def count_adjacent_part2(seats, row, col, n_max):
    cnt = 0
    rows = len(seats)
    cols = len(seats[0])
    for [d_row, d_col] in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1)]:
        for n in range(1, n_max):
            _row = row + n * d_row
            _col = col + n * d_col
            if _row < 0 or _row >= rows or _col < 0 or _col >= cols:
                break

            _seat = seats[_row][_col]
            if _seat == '#':
                cnt += 1
                break
            elif _seat == 'L':
                break

    return cnt
