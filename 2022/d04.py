'''
AoC 2022 Day 4 parts 1 & 2
'''

from sys import argv

def overlaps():
    contains = 0
    overlaps = 0

    with open(argv[1]) as f:
        for d in f.readlines():
            pairs = [p.strip().split('-') for p in d.split(',')]
            p00, p01 = int(pairs[0][0]), int(pairs[0][1])
            p10, p11 = int(pairs[1][0]), int(pairs[1][1])

            if p00 <= p10 and p01 >= p11 or p00 >= p10 and p01 <= p11:
                contains += 1
                overlaps += 1
            elif p00 <= p11 and p01 >= p10:
                overlaps += 1

    return contains, overlaps

def main():
    i, j = overlaps()
    print('AoC \'22 - Day 4\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
