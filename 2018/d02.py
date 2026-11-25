'''
AoC 2018 Day 2 Parts 1 & 2
'''

from sys import argv
from collections import Counter

twos = threes = 0

def count(id):
    global twos, threes

    c = Counter(id).values()

    if 2 in c:
        twos += 1
    if 3 in c:
        threes += 1

def similar(id_1, id_2):
    s = ''

    for i in range(len(id_1)):
        if id_1[i] == id_2[i]:
            s += id_1[i]

    return s

def id_compare(ids):
    i = 0

    while i < len(ids) - 1:
        id_1 = ids[i]
        j = i + 1
        l = len(id_1)

        while j < len(ids):
            id_2 = ids[j]

            if sum([int(id_1[k] == id_2[k]) for k in range(l)]) + 1 == l:
                return similar(id_1, id_2)

            j += 1
        i += 1

def main():
    with open(argv[1]) as f:
        ids = [id.strip() for id in f.readlines()]
    
    for id in ids:
        count(id)

    print(f'Day 1: {twos * threes}\nDay 2: {id_compare(ids)}')

if __name__ == '__main__':
    main()
