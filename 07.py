import re

ROOT = 'shiny gold'


def part1(data):
    G = parse(data)

    cnt = 0
    for root in G.keys() - set([ROOT]):
        cnt += int(contains(G, root, ROOT))

    return cnt


def contains(tree, root, key):
    if root is None:
        return False
    if root == key:
        return True
    else:
        return any([contains(tree, new, key) for (_, new) in tree[root]])


def part2(data):
    return bag_count(parse(data), ROOT)


def bag_count(tree, root):
    if root is None:
        return 0
    else:
        return sum([(int(c) + int(c) * bag_count(tree, new))
                    for (c, new) in tree[root]])


def parse(data):
    G = {}
    for d in data:
        root = re.findall(r'^(\w+ \w+)', d)[0]
        children = []
        if 'no other' in d:
            children = [(0, None)]
        else:
            children = [
                (int(count), color)
                for _, count, color in re.findall(r'((\d) (\w+ \w+))', d)
            ]

        G[root] = children

    return G
