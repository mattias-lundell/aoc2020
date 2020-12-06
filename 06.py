def part1(data):
    return sum([len(set(answer.replace('\n', ''))) for answer in prep(data)])


def prep(data):
    return '\n'.join(data).split('\n\n')


def part2(data):
    return sum([
        len(
            set.intersection(
                *[set(answer) for answer in (answers.split('\n'))]))
        for answers in prep(data)
    ])
