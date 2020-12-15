def part1(data):
    seen = {}

    t0 = 0
    d = -1
    for t0, d in enumerate(data[0].split(',')):
        d = int(d)
        seen[d] = (t0 + 1, t0 + 1)
        last = d

    last = d
    for t in range(t0 + 2, 2020 + 1):
        (t1, t2) = seen[last]
        if t1 == t2 and t1 == t - 1:  # new
            (t1, t2) = seen[0]
            seen[0] = (t2, t)
            last = 0
        else:
            last = t2 - t1
            if last in seen:
                (t1, t2) = seen[last]
            else:
                (t1, t2) = (t, t)
            seen[last] = (t2, t)

    return last


def part2(data):
    seen = {}

    t0 = 0
    d = -1
    for t0, d in enumerate(data[0].split(',')):
        d = int(d)
        seen[d] = (t0 + 1, t0 + 1)
        last = d

    last = d
    for t in range(t0 + 2, 30000000 + 1):
        (t1, t2) = seen[last]
        if t1 == t2 and t1 == t - 1:  # new
            (t1, t2) = seen[0]
            seen[0] = (t2, t)
            last = 0
        else:
            last = t2 - t1
            if last in seen:
                (t1, t2) = seen[last]
            else:
                (t1, t2) = (t, t)
            seen[last] = (t2, t)

    return last
