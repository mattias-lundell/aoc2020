def part1(data):
    def step(d, orientation, x, y):
        action = d[0]
        value = int(d[1:])

        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            orientation = (orientation - value) % 360
        elif action == 'R':
            orientation = (orientation + value) % 360
        elif action == 'F':
            direction = {
                0: 'N',
                90: 'E',
                180: 'S',
                270: 'W',
            }[orientation]
            return step(f'{direction}{value}', orientation, x, y)

        return orientation, x, y

    orientation = 90
    x = y = 0

    for d in data:
        orientation, x, y = step(d, orientation, x, y)

    return abs(x) + abs(y)


def part2(data):
    def step(d, wx, wy, sx, sy):
        action = d[0]
        value = int(d[1:])

        if action == 'N':
            wy += value
        elif action == 'S':
            wy -= value
        elif action == 'E':
            wx += value
        elif action == 'W':
            wx -= value
        elif action == 'L':
            (wx, wy) = {
                90: (-wy, wx),
                180: (-wx, -wy),
                270: (wy, -wx),
            }[value]
        elif action == 'R':
            (wx, wy) = {
                90: (wy, -wx),
                180: (-wx, -wy),
                270: (-wy, wx),
            }[value]
        elif action == 'F':
            sx += value * wx
            sy += value * wy

        return wx, wy, sx, sy

    sx = sy = 0
    x = 10
    y = 1

    for d in data:
        x, y, sx, sy = step(d, x, y, sx, sy)

    return abs(sx) + abs(sy)
