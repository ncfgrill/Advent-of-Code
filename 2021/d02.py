'''
AoC 2021 Day 2 parts 1 & 2
'''

def calc_loc():
    h, d, a = 0, 0, 0

    with open('d02') as f:
        for l in f.readlines():
            l = l.split(' ')
            m, i = l[0], int(l[1])
            if m == 'forward':
                h += i
                d += a * i
            elif m == 'up':
                a -= i
            else:
                a += i
    return h * a, h * d

def main():
    i, j = calc_loc()
    print('AoC \'21 - Day 2\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
