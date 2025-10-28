'''
AoC 2020 Day 5 parts 1 & 2
'''

from sys import argv

seat_ids = []

def analyze(line):
    row_range = [0, 127]
    col_range = [0, 7]

    for c in line:
        row_change = (row_range[1] - row_range[0] + 1) // 2
        col_change = (col_range[1] - col_range[0] + 1) // 2
        match c:
            case 'B':
                row_range[0] += row_change
            case 'F':
                row_range[1] -= row_change
            case 'R':
                col_range[0] += col_change
            case 'L':
                col_range[1] -= col_change

    seat_id = row_range[0] * 8 + col_range[0]
    seat_ids.append(seat_id)
    return seat_id

def solve():
    max_id = 0

    with open(argv[1]) as f:
        for line in f.readlines():
            max_id = max(max_id, analyze(line.strip()))

    return max_id

def find_missing():
    seat_ids.sort()
    for i, seat_id in enumerate(seat_ids):
        if seat_ids[i+1] != seat_id + 1:
            return seat_id + 1

def main():
    print(f'Part 1: {solve()}\nPart 2: {find_missing()}')

if __name__ == '__main__':
    main()
