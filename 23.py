def part1(data):
    digits = [int(c) for c in data[0]]
    ring = {a: b for a, b in zip(digits, digits[1:] + digits[:1])}

    curr = digits[0]

    for _ in range(10):
        a = ring[curr]
        b = ring[a]
        c = ring[b]
        d = ring[c]

        ring[curr] = d

        dest = curr - 1
        while dest in [a, b, c]:
            dest -= 1
        if dest == 0:
            dest = max(set(digits) - set([a, b, c]))

        ring[c] = ring[dest]
        ring[dest] = a
        curr = ring[curr]

    a = ring[1]
    b = ring[a]
    c = ring[b]
    d = ring[c]
    e = ring[d]
    f = ring[e]
    g = ring[f]
    h = ring[g]

    return ''.join([str(i) for i in [a, b, c, d, e, f, g, h]])


def part2(data):
    digits = [int(c) for c in data[0]] + list(range(10, 1000001))
    ring = {a: b for a, b in zip(digits, digits[1:] + digits[:1])}
    curr = digits[0]

    digits_s = set(digits)
    max_d = max(digits)

    for _ in range(10000000):
        a = ring[curr]
        b = ring[a]
        c = ring[b]
        d = ring[c]

        ring[curr] = d

        dest = curr - 1
        while dest in [a, b, c]:
            dest -= 1
        if dest == 0:
            dest = max(digits_s - set([a, b, c]))

        ring[c] = ring[dest]
        ring[dest] = a
        curr = ring[curr]

    a = ring[1]
    b = ring[a]

    return a * b
