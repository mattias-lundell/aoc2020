import re
from collections import Counter


def part1(data):
    acc = 0
    for line in data:
        m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        min_count = int(m.group(1))
        max_count = int(m.group(2))
        char = m.group(3)
        password = m.group(4)

        count = Counter(password)[char]

        if count >= min_count and count <= max_count:
            acc += 1

    return acc


def part2(data):
    acc = 0
    for line in data:
        m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        i1 = int(m.group(1)) - 1
        i2 = int(m.group(2)) - 1
        char = m.group(3)
        password = m.group(4)

        if (password[i1] == char) ^ (password[i2] == char):
            acc += 1

    return acc
