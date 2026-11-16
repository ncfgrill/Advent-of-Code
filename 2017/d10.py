'''
AoC 2017 Day 10 Parts 1 & 2
'''

from math import prod
from sys import argv

SIZE = 256
knot = list(range(SIZE))

def modify_knot(skip, length, position):
    global knot

    knot = knot[position:] + knot[:position]
    knot = list(reversed(knot[:length])) + knot[length:]
    knot = knot[SIZE - position:] + knot[:SIZE - position]
    
    return (position + skip + length) % SIZE

def dense_hash():
    global knot

    dense_hash = []
    i = 0
    
    while i < SIZE:
        j = 1
        hash = knot[i]
        while j < 16:
            hash ^= knot[i + j]
            j += 1

        dense_hash.append(hash)
        i += 16

    return dense_hash

def knot_hash(dense_hash):
    return ''.join([format(h, '02x') for h in dense_hash])

def main():
    global knot

    with open(argv[1]) as f:
        length_string = f.readline().strip()
    
    lengths = [int(x) for x in length_string.split(',')]

    position = 0
    for skip, length in enumerate(lengths):
        position = modify_knot(skip, length, position)

    simple_knot = knot

    knot = list(range(SIZE))
    new_lengths = [17, 31, 73, 47, 23]
    lengths = [ord(c) for c in length_string] + new_lengths

    position = 0
    for i in range(64):
        for skip, length in enumerate(lengths):
            position = modify_knot(skip + i * len(lengths), length, position)

    print(f'Day 1: {prod(simple_knot[:2])}\nDay 2: {knot_hash(dense_hash())}')

if __name__ == '__main__':
    main()
