'''
AoC 2015 Day 24 Parts 1 & 2
'''

from itertools import combinations
from math import prod, inf
from sys import argv

target, weights = 0, []

def get_weights():
    global weights, perms

    with open(argv[1]) as f: weights = f.readlines()
    weights = [int(w.strip()) for w in weights]

def find_groups():
    global target, weights

    qe, i = inf, 3
    while i <= len(weights):
        for j, c in enumerate(list(combinations(weights, i))):
            if j == 0 and sum(c) > target: return qe
            if sum(c) != target: continue
            qe = min(qe, prod(c))
        i += 1

    return qe

#    516 (113, 109, 107, 103, 83, 1)
#    516 (101, 97, 89, 79, 73, 23, 19, 17, 13, 5)
#    516 (71, 67, 61, 59, 53, 47, 43, 41, 31, 29, 11, 3)

def main():
    global target, weights

    get_weights()
    target = sum(weights) // 3
    print('Three groups:', find_groups())

    target = sum(weights) // 4
    print('Four groups:', find_groups())

if __name__ == "__main__":
    main()
