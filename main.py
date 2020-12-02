import time
import math


def run(day, year=2020):
    print(f"AOC {year} Day {day}")
    print()

    padded_day = str(day).zfill(2)

    mod = __import__(padded_day)
    data = get_data(f'{padded_day}.txt')
    _test_data = get_data(f'{padded_day}.test')
    part_1_ans = int(_test_data[0])
    part_2_ans = int(_test_data[1])
    test_data = _test_data[2:]

    test_1_res, _ = run_part(1, mod, test_data)
    if test_1_res == part_1_ans:
        res, time = run_part(1, mod, data)
        print_execution(1, res, time)
    else:
        print('fail test 1')
    test_2_res, _ = run_part(2, mod, test_data)
    if test_2_res == part_2_ans:
        res, time = run_part(2, mod, data)
        print_execution(2, res, time)
    else:
        print('fail test 2')


def print_execution(part, res, time):
    print(f"Part {part}")
    print(f"Output: {res}")
    print(f"Output: {time:.4f}ms")
    print()


def get_data(fname):
    try:
        with open(fname, "r") as f:
            data = f.readlines()

    except Exception as e:
        raise ValueError(f"Unable to read file {fname}") from e

    return data


def run_part(part, mod, data):
    funcname = f'part{part}'

    f = getattr(mod, funcname, None)
    if callable(f):
        t0 = time.perf_counter()
        val = f(data)
        t1 = time.perf_counter()
        return val, (t1 - t0) * 1000

    print(f"No {funcname} function")
    return None, 0


import sys

run(int(sys.argv[1]))
