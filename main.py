import time
import math


def run(day, year=2020):
    print(f"AOC {year} Day {day}")

    padded_day = str(day).zfill(2)

    mod = __import__(padded_day)
    data = get_data(f'{padded_day}.txt')

    part_1_time = run_part(1, mod, data)
    part_2_time = run_part(2, mod, data)

    total_time = part_1_time + part_2_time

    if part_1_time != 0 and part_2_time != 0:
        print(f"Total time: {total_time:.4f}ms")


def get_data(fname):
    try:
        with open(fname, "r") as f:
            data = f.readlines()

    except Exception as e:
        raise ValueError(f"Unable to read file {fname}") from e

    print(f"Loaded puzzle input from {fname}\n")
    return data


def run_part(part, mod, data):
    funcname = f'part{part}'

    f = getattr(mod, funcname, None)
    if callable(f):
        print(f"Part {part}")

        t0 = time.perf_counter()
        val = f(data)
        t1 = time.perf_counter()

        print(f"Output: {val}")
        rtime = (t1 - t0) * 1000
        print(f"Time {rtime:.4f}ms\n")
        return rtime
    else:
        print(f"No {funcname} function")
        return 0

    return rtime


import sys

run(int(sys.argv[1]))
