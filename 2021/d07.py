'''
AoC 2021 Day 7 parts 1 & 2
'''

from math import inf

def get_pos():
    with open('d07') as f:
        l = [int(n) for n in f.readline().split(',')]
        return l, min(l), max(l)

def tri(n):
    return (n**2 + n) // 2

def move():
    pos, min_p, max_p = get_pos()
    min_f1, min_f2 = inf, inf

    for i in range(min_p, max_p + 1):
        s1, s2 = 0, 0
        for j in pos:
            s1 += (abs(j - i))
            s2 += tri(abs(j - i))

        min_f1 = min(min_f1, s1)
        min_f2 = min(min_f2, s2)

    return min_f1, min_f2

def main():
    i, j = move()
    print('AoC \'21 - Day 7\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
