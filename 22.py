def part1(data):
    return score(combat(*parse(data)))


def parse(data):
    players = []
    for player, cs in enumerate('\n'.join(data).split('\n\n'), 1):
        cards = [int(c.strip()) for c in cs.split('\n')[1:]]
        players.append(cards)
    return players


def combat(a, b):
    if not a:
        return b
    elif not b:
        return a

    _a = a.pop(0)
    _b = b.pop(0)

    if _a > _b:
        return combat(a + [_a, _b], b)
    return combat(a, b + [_b, _a])


def score(cards):
    return sum([i * c for i, c in enumerate(reversed(cards), 1)])


def part2(data):
    return score(recursive_combat(*parse(data))[1])


def key(a, b):
    return ','.join([str(i) for i in a]) + '#' + ','.join([str(i) for i in b])


def recursive_combat(a, b):
    seen = set()
    while a and b:
        hands = (tuple(a), tuple(b))
        if hands in seen:
            return 1, a
        seen.add(hands)

        _a = a.pop(0)
        _b = b.pop(0)
        if len(a) >= _a and len(b) >= _b:
            winner, _ = recursive_combat(a[:_a].copy(), b[:_b].copy())
            if winner == 1:
                a += [_a, _b]
            else:
                b += [_b, _a]
        else:
            if _a > _b:
                a += [_a, _b]
            else:
                b += [_b, _a]

    if len(a) > len(b):
        return 1, a
    return 2, b
