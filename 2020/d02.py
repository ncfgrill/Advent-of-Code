'''
AoC 2020 Day 2 parts 1 & 2
'''

from operator import xor
from sys import argv

def check_password(line):
    freq, c, password = line[0].split('-'), line[1][0], line[2]
    c_min, c_max = int(freq[0]), int(freq[1])
    p1, p2 = 0, 0

    if password.count(c) in range(c_min, c_max + 1):
        p1 = 1

    check_1, check_2 = password[c_min - 1], password[c_max - 1]
    if (check_1 == c or check_2 == c) and check_1 != check_2:
        p2 = 1

    return p1, p2

def solve():
    p1_sol, p2_sol = 0, 0

    with open(argv[1]) as f:
        for line in f.readlines():
            sol = check_password(line.strip().split())
            p1_sol += sol[0]
            p2_sol += sol[1]

    return p1_sol, p2_sol

def main():
    solution = solve()
    print(f'Part 1: {solution[0]}\nPart 2: {solution[1]}')

if __name__ == '__main__':
    main()
