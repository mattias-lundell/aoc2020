import re
from collections import defaultdict
from itertools import chain


def part1(data):
    valid_values, ruleset, own, nearby = parse(data)

    res = 0
    for d in chain(*nearby):
        if d not in valid_values:
            res += d

    return res


def part2(data):
    valid_values, ruleset, own, nearby = parse(data)

    nearby = [t for t in nearby if all([r in valid_values for r in t])]

    cnt = defaultdict(set)
    for rule_name, r in ruleset.items():
        for i in range(len(ruleset)):
            a = all([ticket[i] in r for ticket in nearby])
            if a:
                cnt[rule_name].add(i)

    mapping = {}
    while len(cnt) > 0:
        for k, v in cnt.items():
            if len(v) == 1:
                _v = v.pop()
                mapping[k] = _v
                for _, v in cnt.items():
                    v.discard(_v)
                break
        cnt.pop(k)

    res = 1
    for k, v in mapping.items():
        if k.startswith('departure'):
            res *= own[v]

    return res


def parse(data):
    valid_values = set()
    ruleset = defaultdict(set)
    tickets = []

    rules_re = re.compile(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)')
    ticket_re = re.compile(r'(\d+)')

    for l in data:
        rule = rules_re.findall(l)
        if len(rule) > 0:
            name, a1, a2, b1, b2 = rule[0]
            for d in range(int(a1), int(a2) + 1):
                ruleset[name].add(d)
                valid_values.add(d)
            for d in range(int(b1), int(b2) + 1):
                ruleset[name].add(d)
                valid_values.add(d)

        else:
            ticket = ticket_re.findall(l)
            if len(ticket) > 0:
                tickets.append([int(x) for x in ticket])

    own = tickets[0]
    nearby = tickets[1:]

    return valid_values, ruleset, own, nearby
