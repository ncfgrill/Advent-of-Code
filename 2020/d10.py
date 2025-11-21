'''
AoC 2020 Day 10 parts 1 & 2
'''

from sys import argv

jolts = []

def find_diffs():
    diff_1, diff_3, i = 0, 0, 1

    while i < len(jolts):
        match jolts[i] - jolts[i-1]:
            case 1:
                diff_1 += 1
            case 3:
                diff_3 += 1
        i += 1

    return diff_1 * diff_3

def find_combs():
    def arr_seq(n):
        match n:
            case 0:
                return 0
            case 1 | 2:
                return 1
            case _:
                return arr_seq(n-1) + arr_seq(n-2) + arr_seq(n-3)

    total = 1
    count, i, j = 1, 0, 0
    length = len(jolts)

    while j+1 < length:
        if jolts[j+1] - jolts[j] < 3 and j+1 < length:
            count += 1
        else:
            total *= arr_seq(count)
            i = j
            count = 1
        j += 1

    return total

def solve():
    global jolts

    with open(argv[1]) as f:
        jolts = [int(x) for x in f.readlines()]

    jolts.append(0)
    jolts.sort()
    jolts.append(jolts[-1] + 3)

    diff = find_diffs()
    comb = find_combs()

    return diff, comb

def main():
    solution = solve()
    print(f'AoC 2020 Day 10\nPart 1: {solution[0]}\nPart 2: {solution[1]}')

if __name__ == '__main__':
    main()
