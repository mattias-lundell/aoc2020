import re


def part1(data):
    c = re.compile(r'(\w+): "(\w)"')
    r = re.compile(r'(\w+): ([\w| ]+)')
    w = re.compile(r'[ab]+')

    rules = {}
    atoms = set(['|', '(', ')'])
    words = []

    for l in data:
        _c = c.findall(l)
        _r = r.findall(l)
        if _c:
            rule, character = _c[0]
            rules[rule] = character
            atoms.add(character)
        elif _r:
            rule, sub_rules = _r[0]
            sub_rules = sub_rules.split(' ')
            rules[rule] = sub_rules
        else:
            if len(l) > 0:
                words.append(l)

    ww = re.compile(expand(rules, atoms, rules['0']))

    return len(list(filter(None, [ww.fullmatch(word) for word in words])))


def expand(rules, atoms, expanded):
    new_expanded = []
    updated = False
    for rule in expanded:
        if rule in atoms:
            new_expanded.append(rule)
        else:
            new_expanded.append('(')
            new_expanded.append(rules[rule])
            new_expanded.append(')')
            updated = True

    if not updated:
        return ''.join(expanded)

    expanded = flatten(new_expanded)

    return expand(rules, atoms, expanded)


def flatten(xs):
    return [item for sublist in xs for item in sublist]
