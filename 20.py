import numpy as np
from collections import Counter
import math


def part1(data):
    tiles = {}
    data = '\n'.join(data)
    for tile_str in data.split('\n\n'):
        lines = tile_str.splitlines()
        tile_id = int(lines[0].replace(':', '').split(' ')[1])
        tiles[tile_id] = [l.strip() for l in lines[1:]]

    cs = corners(tiles)
    print(cs)

    return math.prod(cs)


def part2(data):
    tiles = {}
    data = '\n'.join(data)
    for tile_str in data.split('\n\n'):
        lines = tile_str.splitlines()
        tile_id = int(lines[0].replace(':', '').split(' ')[1])
        tiles[tile_id] = [l.strip() for l in lines[1:]]

    cs = match_corners(tiles)
    print(cs)


def count_edges(tiles):
    cnt = Counter()
    for tile in tiles.values():
        cnt.update(edges(tile))
    for tile in tiles.values():
        cnt.update(edges(tile[::-1]))
    return cnt


def edges(tile):
    return [
        tile[0],
        tile[-1][::-1],  # reverse to make matching easier
        ''.join(row[-1] for row in tile),
        ''.join(row[0] for row in tile[::-1]),
    ]


def edges2(tile):
    return [
        tile[0],
        tile[-1],  # reverse to make matching easier
        ''.join(row[-1] for row in tile),
        ''.join(row[0] for row in tile),
    ]


def edge(tile, side):
    return edges2(tile)[{
        'n': 0,
        's': 1,
        'w': 2,
        'e': 3,
    }[side]]


def flip(tile):
    return [l[::-1] for l in lines]


def flip(tile):
    res = []
    for rownum in range(len(tile)):
        res.append(''.join(l[-1 - rownum] for l in tile))
    return res


def corners(tiles):
    res = []
    counts = count_edges(tiles)
    for tile_id, tile in tiles.items():
        unique = 0
        for edge in edges(tile):
            if counts[edge] == 1:
                unique += 1
        if unique == 2:
            res.append(tile_id)

    return res


from collections import defaultdict
from itertools import combinations


def match_corners(tiles):
    matching_sides = defaultdict(str)
    corners = {}

    for tid_a, tid_b in combinations(tiles, 2):
        tile_a, tile_b = tiles[tid_a], tiles[tid_b]

        for side_a in 'nsew':
            for side_b in 'nsew':
                edge_a, edge_b = edge(tile_a, side_a), edge(tile_b, side_b)
                if edge_a == edge_b or edge_a == edge_b[::-1]:
                    matching_sides[tid_a] += side_a
                    matching_sides[tid_b] += side_b

    for tid, sides in matching_sides.items():
        if len(sides) == 2:
            corners[tid] = sides

    print(corners)
    return corners
