import shlex


def part1(data):
    acc = 0
    for l in data:
        res = eval_part1(l)
        acc += res
    return acc


def eval_part1(d):
    def eval(op, a, b):
        if op == '+':
            return a + b
        elif op == '*':
            return a * b

    stack = []
    acc = 0
    op = '+'
    for i, t in enumerate(list(shlex.shlex(d))):
        if t == '(':
            stack.append((acc, op))
            acc = 0
            op = '+'
        elif t == ')':
            (_acc, _op) = stack.pop(-1)
            acc = eval(_op, acc, _acc)
        elif t == '+':
            op = '+'
        elif t == '*':
            op = '*'
        else:
            acc = eval(op, acc, int(t))
    return acc


def part2(data):
    acc = 0
    for l in data:
        acc += eval_expr(parse(l, ['*', '+']))
    return acc


def eval_expr(e):
    if len(e) == 3:
        (op, a, b) = e
        if op == '+':
            return eval_expr(a) + eval_expr(b)
        elif op == '*':
            return eval_expr(a) * eval_expr(b)
    else:
        return int(e)


def parse(d, operators):
    for operator in operators:
        depth = 0
        for i, c in enumerate(d):
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            elif depth == 0 and c in operator:
                return (
                    c,
                    parse(d[:i], operators),
                    parse(d[i + 1:], operators),
                )
    d = d.strip()
    if d[0] == '(':
        return parse(d[1:-1], operators)
    return d
