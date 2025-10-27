'''
AoC 2024 Day 2 Parts 1 & 2
'''

from sys import argv

inc = range(1,4)
dec = range(-3,0)
mode = None

def set_mode(e1, e2):
    global mode

    if e1 < e2:
        mode = inc
    elif e1 > e2:
        mode = dec
    else:
        mode = None

def validate(report):
    set_mode(report[0], report[1])
    if not mode:
        return False

    for i in range(0, len(report) - 1):
        if report[i+1] - report[i] not in mode:
            return False

    return True

def change(report):
    for i in range(0, len(report)):
        new_report = report[:i] + report[i+1:]
        print(new_report)

        if validate(new_report):
            return 1

    return 0

def check(report):
    if not validate(report):
        return change(report)

    return 2

def main():
    safe = 0
    safe_with_change = 0

    with open(argv[1]) as f:
        for line in f.readlines():
            valid = check([int(i) for i in line.split()])
            if valid == 2:
                safe += 1
                safe_with_change += 1
            elif valid == 1:
                safe_with_change += 1

    print('Part 1:', safe)
    print('Part 2:', safe_with_change)

if __name__ == '__main__':
    main()
