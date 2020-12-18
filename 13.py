def part1(data):
    leave = int(data[0])
    busses = [int(x) for x in data[1].split(',') if x != 'x']

    soonest = [(leave % bus, bus) for bus in busses]

    wait, bus = min(sorted([(-a + bus, bus) for (a, bus) in soonest]))

    return wait * bus


def part2(data):
    '''
    we have series of congruences

    t ≡ minute (mod bus)
    '''

    busses = sorted([(int(bus), minute)
                     for minute, bus in enumerate(data[1].split(','))
                     if bus != 'x'])

    t = 0
    lcm = 1
    for bus, minute in busses:
        while (t + minute) % bus != 0:
            t += lcm
        lcm *= bus
    return t
