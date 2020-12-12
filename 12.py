def part1(data):
    def step(action, value, orientation, x, y):
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
            return step(direction, value, orientation, x, y)

        return orientation, x, y

    orientation = 90
    x = y = 0

    for d in data:
        action = d[0]
        value = int(d[1:])
        orientation, x, y = step(action, value, orientation, x, y)

    return abs(x) + abs(y)


def part2(data):
    def step(action, value, wx, wy, sx, sy):
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
    wx = 10
    wy = 1

    for d in data:
        action = d[0]
        value = int(d[1:])
        wx, wy, sx, sy = step(action, value, wx, wy, sx, sy)

    return abs(sx) + abs(sy)
