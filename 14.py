import re


def part1(data):
    def get_mask(line):
        mask = re.match(r'mask = (\w+)', line)
        sets = {}
        for i, c in enumerate(reversed(mask.group(1))):
            if c != 'X':
                sets[i] = c

        return sets

    pattern = r'mem\[(\d+)\] = (\d+)'
    res = 0
    mem = {}
    sets = {}
    for line in data:
        if line.startswith('mask'):
            sets = get_mask(line)
        else:
            match = re.match(pattern, line)
            addr = int(match.group(1))
            val = list(reversed(list(bin(int(match.group(2)))[2:].zfill(36))))

            for s in sets:
                val[s] = sets[s]

            mem[addr] = val

    for val in mem.values():
        val = ''.join(reversed(val))

        res += int(val, 2)

    return res


def part2(data):
    pattern = r'mem\[(\d+)\] = (\d+)'
    res = 0
    mem = {}
    masks = {}
    for line in data:
        if line.startswith('mask'):
            masks = get_masks(line)
        else:
            match = re.match(pattern, line)
            val = int(match.group(2))

            addr = list(reversed(list(bin(int(match.group(1)))[2:].zfill(36))))
            addrs = addresses(masks, addr)
            for addr in addrs:
                mem[addr] = val

    for val in mem.values():

        res += int(val)

    return res


def addresses(masks, address):
    res = []
    for mask in masks:
        new = address[:]
        for k in mask:
            new[k] = mask[k]
        res.append(''.join(new))
    return res


from itertools import product


def get_masks(line):
    mask = re.match(r'mask = (\w+)', line)
    sets = {}
    floating = []
    masks = []
    for i, c in enumerate(reversed(mask.group(1))):
        if c == '1':
            sets[i] = c
        elif c == 'X':
            floating.append(i)

    for i, a in enumerate(product(('0', '1'), repeat=len(floating))):
        s = {}
        for j, b in enumerate(a):
            s[floating[j]] = b
        masks.append({**sets, **s})

    return masks
