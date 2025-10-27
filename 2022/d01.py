'''
AoC 2022 Day 1 parts 1 & 2
'''

from sys import argv

def count_cals():
    cals = []
    total = 0

    with open(argv[1]) as f:
        for d in f.readlines():
            if d != '\n':
                total += int(d)
            else:
                cals.append(total)
                total = 0

    cals.sort(reverse=True)
    return cals[0], sum(cals[0:3])

def main():
    i, j = count_cals()
    print('AoC \'22 - Day 1\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
