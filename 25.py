def powmod(base, exp, m):
    result = 1

    while (exp > 0):
        if (exp & 1):
            result = (result * base) % m

        base = (base * base) % m
        exp >>= 1

    return result


def part1(data):
    keya = int(data[0])
    keyb = int(data[1])

    m = 20201227

    loopsa = 1
    subja = 7

    while True:
        vala = powmod(subja, loopsa, m)

        if vala == keya:
            break

        loopsa += 1

    valb = 1

    for _ in range(loopsa):
        valb *= keyb
        valb %= m

    print(valb)
    return valb
