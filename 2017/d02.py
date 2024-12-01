'''
Aoc 2017 Day 2 Parts 1 & 2
'''

def find_min_max(row):
    return max(row) - min(row)

def find_divisible(row):
    for i in range(len(row) - 1):
        for j in range(i + 1, len(row)):
            n1, n2 = row[i], row[j]
            if not n1 % n2:
                return n1 // n2
            if not n2 % n1:
                return n2 // n1

def main():
    chksum_m, chksum_d = 0, 0

    with open('d02') as f:
        for line in f.readlines():
            row = [int(n) for n in line.split()]
            chksum_m += find_min_max(row)
            chksum_d += find_divisible(row)

    print('Part 1: {}'.format(chksum_m))
    print('Part 2: {}'.format(chksum_d))

if __name__ == '__main__':
    main()
