def part1(data):
    digits = [int(c) for c in data[0]]
    ring = {a: b for a, b in zip(digits, digits[1:] + digits[:1])}

    ring = solve(digits, ring, 100)
    a = ring[1]
    b = ring[a]
    c = ring[b]
    d = ring[c]
    e = ring[d]
    f = ring[e]
    g = ring[f]
    h = ring[g]

    return ''.join([str(i) for i in [a, b, c, d, e, f, g, h]])


def solve(digits, ring, n):
    curr = digits[0]

    max_d = sorted(digits)[-4:]

    for _ in range(n):
        a = ring[curr]
        b = ring[a]
        c = ring[b]
        d = ring[c]

        ring[curr] = d

        dest = curr - 1
        while dest in [a, b, c]:
            dest -= 1
        if dest == 0:
            dest = max([_d for _d in max_d if _d not in [a, b, c]])

        ring[c] = ring[dest]
        ring[dest] = a
        curr = ring[curr]

    return ring


def part2(data):
    digits = [int(c) for c in data[0]] + list(range(10, 1000001))
    ring = {a: b for a, b in zip(digits, digits[1:] + digits[:1])}

    ring = solve(digits, ring, 10000000)

    a = ring[1]
    b = ring[a]

    return a * b
