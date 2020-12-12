import cmath


def part1(data):
    pos = complex(0, 0)
    orientation = complex(0, 1)

    for d in data:
        action = d[0]
        value = int(d[1:])

        if action == 'N':
            pos += value
        elif action == 'S':
            pos -= value
        elif action == 'E':
            pos += complex(0, value)
        elif action == 'W':
            pos -= complex(0, value)
        elif action == 'L':
            orientation *= degree_to_complex(360 - value)
        elif action == 'R':
            orientation *= degree_to_complex(value)
        elif action == 'F':
            pos += orientation * value

    return int(abs(pos.real) + abs(pos.imag))


def degree_to_complex(degree):
    return {
        90: complex(0, 1),
        180: complex(-1, 0),
        270: complex(0, -1),
    }[degree]


def part2(data):
    pos = complex(0, 0)
    way = complex(1, 10)

    for d in data:
        action = d[0]
        value = int(d[1:])

        if action == 'N':
            way += value
        elif action == 'S':
            way -= value
        elif action == 'E':
            way += complex(0, value)
        elif action == 'W':
            way -= complex(0, value)
        elif action == 'L':
            way *= degree_to_complex(360 - value)
        elif action == 'R':
            way *= degree_to_complex(value)
        elif action == 'F':
            pos += way * value

    return int(abs(pos.real) + abs(pos.imag))
