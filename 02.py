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
    min_cnt, max_cnt, char, pwd = re.match(
        r'(\d+)-(\d+) ([a-z]): ([a-z]+)',
        line,
    ).groups()

    return (int(min_cnt), int(max_cnt), char, pwd)
