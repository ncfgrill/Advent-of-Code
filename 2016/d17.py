'''
AoC 2016 Day 17 parts 1 & 2
'''

from hashlib import md5
from sys import argv

min_steps, max_steps, route = 99999999, 0, ''
good, passcode = 'bcdef', argv[1]

def next_step(r, c, steps, h):
    global min_steps, max_steps, good, passcode, route

    if (r, c) == (3, 3):
        if steps < min_steps: route, min_steps = h[len(passcode):], steps
        max_steps = max(max_steps, steps)
    else:
        check = md5(h.encode()).hexdigest()
        # Check up
        if check[0] in good and r - 1 >= 0:
            next_step(r - 1, c, steps + 1, h + 'U')
        # Check down
        if check[1] in good and r + 1 <= 3:
            next_step(r + 1, c, steps + 1, h + 'D')
        # Check left
        if check[2] in good and c - 1 >= 0:
            next_step(r, c - 1, steps + 1, h + 'L')
        # Check right
        if check[3] in good and c + 1 <= 3:
            next_step(r, c + 1, steps + 1, h + 'R')

def main():
    global passcode, route, max_steps

    next_step(0, 0, 0, passcode)
    print('Shortest path:', route)
    print('Longest path:', max_steps)

if __name__ == "__main__":
    main()
