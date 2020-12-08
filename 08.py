def part1(input):
    data = parse(input)
    visited = set()
    i = 0
    acc = 0
    while True:
        if i in visited:
            return acc
        visited.add(i)
        (instr, delta) = data[i]
        if instr == 'nop':
            i += 1
        elif instr == 'acc':
            acc += delta
            i += 1
        elif instr == 'jmp':
            i += delta


def parse(input):
    data = []
    for row in input:
        row = row.split(' ')
        data.append((row[0], int(row[1])))
    return data


def part2(input):
    data = parse(input)

    for temper in range(len(data)):
        instructions = data[:]
        instruction = instructions[temper]
        if instruction[0] == 'nop':
            instructions[temper] = ('jmp', instruction[1])
        elif instruction[0] == 'jmp':
            instructions[temper] = ('nop', instruction[1])
        else:
            continue

        visited = set()
        i = 0
        acc = 0
        while True:
            if i in visited:
                break
            if i >= len(instructions):
                return acc
            visited.add(i)
            (instr, delta) = instructions[i]
            if instr == 'nop':
                i += 1
            elif instr == 'acc':
                acc += delta
                i += 1
            elif instr == 'jmp':
                i += delta
