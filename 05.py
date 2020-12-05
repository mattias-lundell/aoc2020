# b 0
# f 1

# l 0
# r 1


def part1(data):
    max_seat = -1
    for l in data:
        row = l[:7]
        col = l[7:]

        row = row.replace('B', '1')
        row = row.replace('F', '0')

        col = col.replace('L', '0')
        col = col.replace('R', '1')

        seat = int(row, 2) * 8 + int(col, 2)

        max_seat = max(max_seat, seat)

    return max_seat


def part2(data):
    max_seat = -1
    seats = []
    for l in data:
        row = l[:7]
        col = l[7:]

        row = row.replace('B', '1')
        row = row.replace('F', '0')

        col = col.replace('L', '0')
        col = col.replace('R', '1')

        seats.append(int(row, 2) * 8 + int(col, 2))

    seats = sorted(seats)

    min_seat = min(seats)
    max_seat = max(seats)

    all_seats = set(range(min_seat, max_seat + 1))

    return list((all_seats - set(seats)))[0]
