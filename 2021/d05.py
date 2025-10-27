'''
AoC 2021 Day 5 parts 1 & 2
'''

from sys import argv

vents = {}

def get_coords():
    coords = []
    with open(argv[1]) as f:
        l = f.readline()
        while l:
            c = l.strip('\n').split(' -> ')
            coords.append([list(int(m) for m in c[0].split(',')), list(int(n) for n in c[1].split(','))])
            l = f.readline()
    return coords

def count_vents():
    s = 0
    for n in vents.values():
        if n > 1: s += 1

    return s

def find_vents():
    coords = get_coords()
    for c in coords:
        d = 1
        if c[0][0] == c[1][0]:
            if c[0][1] > c[1][1]: d = -1
            for x in range(c[0][1], c[1][1] + d, d):
                p = (c[0][0], x)
                if p in vents: vents[p] += 1
                else: vents[p] = 1
        elif c[0][1] == c[1][1]:
            if c[0][0] > c[1][0]: d = -1
            for x in range(c[0][0], c[1][0] + d, d):
                p = (x, c[0][1])
                if p in vents: vents[p] += 1
                else: vents[p] = 1
        else:
            d1, d2 = 1, 1
            if c[0][0] > c[1][0]: d1 = -1
            if c[1][0] > c[1][1]: d2 = -1
            for x in range(0, c[0][0] - c[1][0] + d1, d1):
                p = (c[0][0] + x*d1, c[0][1] + x*d2)
                print(p)
                if p in vents: vents[p] += 1
                else: vents[p] = 1

    return count_vents()

def main():
    i = find_vents()
    print('AoC \'21 - Day 5\n  P1: {}\n  P2: '.format(i))

if __name__ == '__main__':
    main()
