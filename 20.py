import numpy as np
from collections import Counter


def part1(data):
    tiles = {}
    data = '\n'.join(data)
    for tile_str in data.split('\n\n'):
        lines = tile_str.splitlines()
        tile_id = int(lines[0].replace(':', '').split(' ')[1])
        tiles[tile_id] = [l.strip() for l in lines[1:]]
    return corners(tiles)


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
        tile[-1][::-1],
        ''.join(row[-1] for row in tile),
        ''.join(row[0] for row in tile[::-1]),
    ]


def corners(tiles):
    res = 1
    counts = count_edges(tiles)
    for tile_id, tile in tiles.items():
        unique = 0
        for edge in edges(tile):
            if counts[edge] == 1:
                unique += 1
        if unique == 2:
            print(tile_id)
            res *= tile_id

    print()
    return res
