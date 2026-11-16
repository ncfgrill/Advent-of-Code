'''
AoC 2017 Day 9 Parts 1 & 2
'''

from sys import argv

def evaluate(line):
    in_garbage = False
    value = 0
    group_total = 0
    garbage_total = 0

    i = 0
    while i < len(line):
        c = line[i]

        if not in_garbage:
            match c:
                case '<':
                    in_garbage = True
                case '{':
                    value += 1
                case '}':
                    group_total += value
                    value -= 1
        else:
            match c:
                case '!':
                    i += 1
                case '>':
                    in_garbage = False
                case _:
                    garbage_total += 1

        i += 1

    return group_total, garbage_total

def main():
    group_sum = 0

    with open(argv[1]) as f:
        totals = evaluate(f.readline().strip())
    print(f'Day 1: {totals[0]}\nDay 2: {totals[1]}')

if __name__ == '__main__':
    main()
