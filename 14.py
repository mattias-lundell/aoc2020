import re
from itertools import product

mask_re = re.compile(r'mask = (\w+)')
mem_re = re.compile(r'mem\[(\d+)] = (\d+)')


def get_mask(line):
    mask = mask_re.match(line)
    sets = {}
    for i, c in enumerate(reversed(mask.group(1))):
        if c != 'X':
            sets[i] = c

    return sets


def part1(data):
    res = 0
    mem = {}
    sets = {}
    for line in data:
        if line.startswith('mask'):
            sets = get_mask(line)
        else:
            match = mem_re.match(line)

            addr = int(match.group(1))
            val = int(match.group(2))

            val = list(reversed(list(bin(val)[2:].zfill(36))))
            for s in sets:
                val[s] = sets[s]

            mem[addr] = int(''.join(reversed(val)), 2)

    return sum(mem.values())


def part2(data):
    res = 0
    mem = {}
    masks = {}
    for line in data:
        if line.startswith('mask'):
            masks = get_masks(line)
        else:
            match = mem_re.match(line)

            addr = int(match.group(1))
            val = int(match.group(2))

            addr = list(reversed(list(bin(addr)[2:].zfill(36))))
            addrs = addresses(masks, addr)
            for addr in addrs:
                mem[addr] = val

    return sum(mem.values())


def addresses(masks, address):
    res = []
    for mask in masks:
        new = address[:]
        for k in mask:
            new[k] = mask[k]
        res.append(''.join(new))
    return res


def get_masks(line):
    mask = mask_re.match(line)
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
