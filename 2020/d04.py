'''
AoC 2020 Day 4 parts 1 & 2
'''

from sys import argv

def validate(code, value):
    match code:
        case 'byr':
            if len(value) == 4 and int(value) in range(1920, 2003):
                return 1
        case 'iyr':
            if len(value) == 4 and int(value) in range(2010, 2021):
                return 1
        case 'eyr':
            if len(value) == 4 and int(value) in range(2020, 2031):
                return 1
        case 'hgt':
            if value[-2:] == 'cm':
                if int(value[:-2]) in range(150, 194):
                    return 1
            elif value[-2:] == 'in':
                if int(value[:-2]) in range(59, 77):
                    return 1
        case 'hcl':
            if len(value) == 7 and value[0] == '#':
                for c in value[1:]:
                    if c not in '0123456789abcdef':
                        break
                    return 1
        case 'ecl':
            if value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                return 1
        case 'pid':
            if len(value) == 9:
                return 1
    return 0

def check(info):
    total_1, total_2 = 0, 0

    for item in info:
        for i in item.split(' '):
            values = i.split(':')
            code, value = values[0].strip(), values[1].strip()
            if code != 'cid':
                total_1 += 1
                if validate(code, value):
                    total_2 += 1

    return int(total_1 == 7), int(total_2 == 7)

def solve():
    info, valid_1, valid_2 = [], 0, 0

    with open(argv[1]) as f:
        for line in f.readlines():
            if line.strip():
                info.append(line)
            else:
                result = check(info)
                valid_1 += result[0]
                valid_2 += result[1]
                info.clear()
        result = check(info)
        valid_1 += result[0]
        valid_2 += result[1]

    return valid_1, valid_2

def main():
    solution = solve()
    print(f'Part 1: {solution[0]}\nPart 2: {solution[1]}')

if __name__ == '__main__':
    main()
