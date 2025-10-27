'''
AoC 2021 Day 3 parts 1 & 2
'''

from sys import argv

def get_data():
    with open(argv[1]) as f:
        return [l.strip('\n') for l in f.readlines()]

def rating(data, lm, i):
    if len(data) == 1: return data[0]

    t0, t1 = 0, 0
    zero, one = [], []
    for j in range(len(data)):
        if data[j][i] == '0':
            t0 += 1
            zero.append(data[j])
        else:
            t1 += 1
            one.append(data[j])

    if lm == 0: return rating(zero if t0 <= t1 else one, lm, i+1)
    else: return rating(zero if t0 > t1 else one, lm, i+1)

def calc():
    data = get_data()
    gamma, epsilon = '', ''
    zero, one = [], []

    for i in range(len(data[0])):
        t0, t1 = 0, 0
        for j in range(len(data)):
            if data[j][i] == '0':
                t0 += 1
                if i == 0: zero.append(data[j])
            else:
                t1 += 1
                if i == 0: one.append(data[j])
        if t0 > t1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    
    lm = (1, 0) if len(zero) > len(one) else (0, 1)
    return int(gamma, 2) * int(epsilon, 2), (int(rating(zero, lm[0], 1), 2) * int(rating(one, lm[1], 1), 2))

def main():
    i, j = calc()
    print('AoC \'21 - Day 3\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
