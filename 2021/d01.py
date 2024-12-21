'''
AoC 2021 Day 1 parts 1 & 2
'''

def get_data():
    with open('d01') as f:
        return [int(d.strip('\n')) for d in f.readlines()]

def check_data():
    inc_1, inc_2, check = 0, 0, 999999
    data = get_data()

    for i, d in enumerate(data):
        if d > check: inc_1 += 1
        check = d

        if i < len(data) - 3 and data[i+3] > data[i]: inc_2 += 1
    return inc_1, inc_2

def main():
    i, j = check_data()
    print('AoC \'21 - Day 1\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
