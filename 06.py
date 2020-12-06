def part1(data):
    sum = 0
    for answer in [x.replace('\n', '') for x in '\n'.join(data).split('\n\n')]:
        sum += len(set(answer))

    return sum


def part2(data):
    sum = 0
    for answer in [x for x in '\n'.join(data).split('\n\n')]:
        sum += len(set.intersection(*[set(a) for a in (answer.split('\n'))]))

    return sum
