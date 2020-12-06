from re import match, search

with open("input.txt") as fo:
    passports = []
    l = ""
    for line in fo:
        if line == "\n":
            passports.append(l)
            l = ""
        else:
            l += line.rstrip() + " "


fields = {'byr': None, 'iyr': None, 'eyr': None, 'hgt': None, 'hcl': None, 'ecl': None, 'pid': None, 'cid': None}


def scanPassportPart1(passportStr):
    passport_fields = fields.copy()
    for field in passportStr:
        passport_fields[field[:3]] = field[4:]
    for key in passport_fields.keys():
        if key == 'cid':
            continue
        if passport_fields[key] is None:
            return False
    return True


def part1():
    validPassports = 0
    for pp in passports:
        if scanPassportPart1(pp.split(" ")):
            validPassports += 1
    return validPassports


def part2():
    validPassports = 0
    for pp in passports:
        if scanPassportPart2(pp.split(" ")):
            validPassports += 1
    return validPassports


def scanPassportPart2(passportStr):
    passport_fields = fields.copy()
    for field in passportStr:
        passport_fields[field[:3]] = field[4:]

    for key in passport_fields:
        if key == 'cid':
            continue
        if passport_fields[key] is None:
            return False

    if not 1920 <= int(passport_fields['byr']) <= 2002:
        return False
    if not 2010 <= int(passport_fields['iyr']) <= 2020:
        return False
    if not 2020 <= int(passport_fields['eyr']) <= 2030:
        return False
    if not match('^(59|6\d|7[0-6])in|(1[5-9]\d|19[0-3])cm$', passport_fields['hgt']):
        return False
    if search(r'\b{ecl}'.format(**passport_fields), 'amb blu brn gry grn hzl oth') is None:
        return False
    if match("#[\da-f]{6}", passport_fields['hcl']) is None:
        return False
    if len(passport_fields['pid']) != 9:
        return False
    return True


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
