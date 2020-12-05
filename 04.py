import re

patterns = {
    "byr": "19[2-9][0-9]|200[0-2]",
    "iyr": "20(1[0-9]|20)",
    "eyr": "20(2[0-9]|30)",
    "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
    "hcl": "#[0-9a-f]{6}",
    "ecl": "amb|blu|brn|gry|grn|hzl|oth",
    "pid": "[0-9]{9}",
    "cid": ".*"
}


def part1(data):
    cnt = 0
    for passport in get_passports(data):
        if validate_keys(passport):
            cnt += 1

    return cnt


def get_passports(data):
    passports = []
    passport = {}
    for w in data:
        if w == '':
            passports.append(passport)
            passport = {}
        else:
            passport.update(
                {k: v
                 for k, v in [x.split(':') for x in w.split(' ')]})
    passports.append(passport)

    return passports


def validate_keys(passport):
    missing = (set(patterns)) - (set(passport.keys()))

    return len(missing) == 0 or missing == set(['cid'])


def validate(passport):
    if validate_keys(passport):
        for k, v in passport.items():
            if re.fullmatch(patterns[k], v) is None:
                return False
        return True
    return False


def part2(data):
    cnt = 0
    for passport in get_passports(data):
        if validate(passport):
            cnt += 1
    return cnt
