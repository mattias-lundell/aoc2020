def part1(data):
    players = []
    for player, cs in enumerate('\n'.join(data).split('\n\n'), 1):
        cards = [int(c.strip()) for c in cs.split('\n')[1:]]
        players.append(cards)

    return score(play(*players))


def play(a, b):
    print(a, b)
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a

    _a = a.pop(0)
    _b = b.pop(0)

    if _a > _b:
        return play(a + [_a, _b], b)
    return play(a, b + [_b, _a])


def score(cards):
    return sum([i * c for i, c in enumerate(reversed(cards), 1)])
