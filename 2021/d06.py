'''
AoC 2021 Day 6 parts 1 & 2
'''

def create_fish():
    f = [0 for x in range(9)]
    with open('d06') as fi:
        for l in [int(x) for x in fi.readline().split(',')]:
            f[l] += 1

    d, save = 0, 0
    while d < 256:
        if d == 80:
            save = sum(f)
        f[8], f[7], f[6], f[5], f[4], f[3], f[2], f[1], f[0] \
                = f[0], f[8], f[7], f[6], f[5], f[4], f[3], f[2], f[1]
        f[6] += f[8]

        d += 1

    return save, sum(f)
def main():
    i, j = create_fish()
    print('AoC \'21 - Day 6\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
