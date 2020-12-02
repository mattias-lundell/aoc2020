import re
from collections import Counter


def part1(data):
    acc = 0
    for line in data:
        (min_count, max_count, char, password) = parse(line)

        count = Counter(password)[char]

        if count >= min_count and count <= max_count:
            acc += 1

    return acc


def part2(data):
    acc = 0
    for line in data:
        (i, j, char, password) = parse(line)

        if (password[i - 1] == char) ^ (password[j - 1] == char):
            acc += 1

    return acc


def parse(line):
    m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
    min_count = int(m.group(1))
    max_count = int(m.group(2))
    char = m.group(3)
    password = m.group(4)

    return (min_count, max_count, char, password)
