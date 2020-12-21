import re
from collections import defaultdict, Counter

line_re = re.compile(r'([a-z ]+) \(contains ([a-z, ]+)\)')


def part1(data):
    atoi, all_ingredients = solve(data)

    all_ingredients_cnt = Counter(all_ingredients)

    used = set()
    for ingredients in atoi.values():
        used.update(ingredients)

    return sum(
        [all_ingredients_cnt[k] for k in (all_ingredients_cnt.keys() - used)])


def part2(data):
    atoi, _ = solve(data)

    return ','.join([list(atoi[k])[0] for k in sorted(atoi.keys())])


def solve(data):
    atoi = defaultdict(set)
    all_ingredients = []

    for line in data:
        a, b = line_re.findall(line)[0]
        ingredients, allergenes = a.split(' '), b.split(', ')
        all_ingredients.extend(ingredients)

    for line in data:
        a, b = line_re.findall(line)[0]
        ingredients, allergenes = a.split(' '), b.split(', ')
        for a in allergenes:
            atoi[a] = set(all_ingredients)

    for line in data:
        a, b = line_re.findall(line)[0]
        ingredients, allergenes = a.split(' '), b.split(', ')
        for a in allergenes:
            atoi[a] = atoi[a].intersection(ingredients)

    def_yes = set()

    for ingredients in atoi.values():
        if len(ingredients) == 1:
            def_yes.update(ingredients)

    while True:
        temp = {}
        for allergene, ingredients in atoi.items():
            if len(ingredients - def_yes) == 1:
                temp[allergene] = ingredients - def_yes

        if len(temp) == 0:
            break

        for allergene, ingredients in temp.items():
            atoi[allergene] = ingredients
            def_yes.update(ingredients)

    used = set()
    for ingredients in atoi.values():
        used.update(ingredients)

    return atoi, all_ingredients
