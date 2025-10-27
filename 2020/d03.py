'''
AoC 2020 Day 3 parts 1 & 2
'''

from math import prod
from sys import argv

def solve():
    with open(argv[1]) as f:
        forest = [line.strip() for line in f.readlines()]

    i = [0, 0, 0, 0, 0]
    trees = [0, 0, 0, 0, 0]
    for l, line in enumerate(forest):
        inc = 1
        for j in range(0, len(i)):
            if j != len(i) - 1:
                if line[i[j]] == '#':
                    trees[j] += 1
                i[j] = (i[j] + inc) % len(line)
            else:
                if not (l % 2):
                    if line[i[j]] == '#':
                        trees[j] += 1
                    i[j] = (i[j] + 1) % len(line)
            inc += 2

    return trees[1], prod(trees)

def main():
    solution = solve()
    print(f'Part 1: {solution[0]}\nPart 2: {solution[1]}')

if __name__ == '__main__':
    main()
