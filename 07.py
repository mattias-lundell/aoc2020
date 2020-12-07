import re


def part1(data):
    tree = {}
    for d in data:
        d = d.replace('bags', '').replace('bag', '').replace('.', '')
        re.match(r'(\w+) bags contain (\d \w \w)+', d)
        d = [a.strip() for a in d.split('contain')]
        head = d[0]
        tail = [a.strip() for a in d[1].split(',')]
        tail = [(a.split(' ')[0], ' '.join(a.split(' ')[1:])) for a in tail]
        if tail == [('no', 'other')]:
            tail = [(0, None)]

        tree[head] = tail

    cnt = 0
    for root in tree.keys():
        if root != 'shiny gold':
            if contains(tree, root, 'shiny gold'):
                cnt += 1

    return cnt


def contains(tree, root, key):
    if root is None:
        return False
    if root == key:
        return True
    else:
        return any([contains(tree, new, key) for (_, new) in tree[root]])


def part2(data):
    tree = {}
    for d in data:
        d = d.replace('bags', '').replace('bag', '').replace('.', '')
        re.match(r'(\w+) bags contain (\d \w \w)+', d)
        d = [a.strip() for a in d.split('contain')]
        head = d[0]
        tail = [a.strip() for a in d[1].split(',')]
        tail = [(a.split(' ')[0], ' '.join(a.split(' ')[1:])) for a in tail]
        if tail == [('no', 'other')]:
            tail = [(0, None)]

        tree[head] = tail

    return s(tree, 'shiny gold')


def s(tree, root):
    if root is None:
        return 0
    else:
        return sum([(int(c) + int(c) * s(tree, new))
                    for (c, new) in tree[root]])
