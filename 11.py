def part1(data):
    seats = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            seats[(i, j)] = data[i][j]

    cnt = 0
    while True:
        next_gen = step(seats)
        if next_gen == seats:
            return count_occupied(seats.values())
        seats = next_gen
        cnt += 1


def print_seats(seats, n_i, n_j):
    for i in range(n_i):
        row = []
        for j in range(n_j):
            row.append(seats[(i, j)])
        print(''.join(row))
    print()


def step(seats):
    next_gen = {}
    for seat in seats:
        cnt = count_occupied(adjacent(seats, seat))
        if seats[seat] == 'L':
            if cnt == 0:
                next_gen[seat] = '#'
            else:
                next_gen[seat] = 'L'
        elif seats[seat] == '#':
            if cnt >= 4:
                next_gen[seat] = 'L'
            else:
                next_gen[seat] = '#'
        else:
            next_gen[seat] = seats[seat]
    return next_gen


def count_occupied(xs):
    cnt = 0
    for x in xs:
        if x == '#':
            cnt += 1

    return cnt


def adjacent(seats, seat):
    (i, j) = seat
    res = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            else:
                res.append(seats.get((i + di, j + dj), '.'))

    return res


def part2(data):
    seats = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            seats[(i, j)] = data[i][j]

    cnt = 0
    while True:
        next_gen = step2(seats, max(len(data), len(data[0])), cnt)
        if next_gen == seats:  # or cnt > 1:
            return count_occupied(seats.values())
        seats = next_gen
        cnt += 1


def step2(seats, ray_len, step):
    next_gen = {}
    for seat in seats:
        cnt = count_adjacent_part2(seats, seat, ray_len, step)
        if seats[seat] == 'L':
            if cnt == 0:
                next_gen[seat] = '#'
            else:
                next_gen[seat] = 'L'
        elif seats[seat] == '#':
            if cnt >= 5:
                next_gen[seat] = 'L'
            else:
                next_gen[seat] = '#'
        else:
            next_gen[seat] = seats[seat]
    return next_gen


def count_adjacent_part2(seats, seat, n_max, step):
    (i, j) = seat
    res = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            else:
                for n in range(1, n_max):
                    _i = i + n * di
                    _j = j + n * dj
                    _seat = seats.get((_i, _j), '.')
                    if _seat in ['#', 'L']:
                        if _seat == '#':
                            res.append('#')
                        break

    return len(res)
