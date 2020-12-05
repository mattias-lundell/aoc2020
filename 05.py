# b 0
# f 1

# l 0
# r 1


def part1(data):
    return max(get_seats(data))


def get_seats(data):
    seats = []
    for line in data:
        row = line[:7].replace('B', '1').replace('F', '0')
        col = line[7:].replace('L', '0').replace('R', '1')

        seats.append(int(row, 2) * 8 + int(col, 2))

    return sorted(seats)


def part2(data):
    seats = set(get_seats(data))
    all_seats = set(range(min(seats), max(seats) + 1))

    return (all_seats - seats).pop()
