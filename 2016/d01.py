'''
AoC 2016 Day 1 Parts 1 & 2
'''

from sys import argv

directions = []

def get_directions():
    global directions

    with open(argv[1]) as f:
        directions = f.readline().split(', ')

    for i, d in enumerate(directions):
        directions[i] = (directions[i][0], int(directions[i][1:].strip()))

def travel():
    global directions

    c_d = 0 # North 0, East 1, South 2, West 3
    ns, ew = 0, 0 # North-South, East-West displacement
    visited, loc, found = set(), (), False

    for d in directions:
        past = (ns, ew)
        if c_d == 0: # North
            if d[0] == 'R':
                ew += d[1]
                c_d = (c_d + 1) % 4
                if not found:
                    for i in range(past[1] + 1, ew + 1):
                        curr = (past[0], i)
                        if curr in visited: loc, found = curr, True
                        else: visited.add(curr)
            else:
                ew -= d[1]
                c_d = (c_d - 1) % 4
                if not found:
                    for i in range(ew, past[1]):
                        curr = (past[0], i)
                        if curr in visited: loc, found = curr, True
                        else: visited.add(curr)
        elif c_d == 1: # East
            if d[0] == 'R':
                ns -= d[1]
                c_d = (c_d + 1) % 4
                if not found:
                    for i in range(ns, past[0]):
                        curr = (i, past[1])
                        if curr in visited: loc, found = curr, true
                        else: visited.add(curr)
            else:
                ns += d[1]
                c_d = (c_d - 1) % 4
                if not found:
                    for i in range(past[0] + 1, ns + 1):
                        curr = (i, past[1])
                        if curr in visited: loc, found = curr, True
                        else: visited.add(curr)
        elif c_d == 2: # South
            if d[0] == 'R':
                ew -= d[1]
                c_d = (c_d + 1) % 4
                if not found:
                    for i in range(ew, past[1]):
                        curr = (past[0], i)
                        if curr in visited: loc, found = curr, True
                        else: visited.add(curr)
            else:
                ew += d[1]
                c_d = (c_d - 1) % 4
                if not found:
                    for i in range(past[1] + 1, ew + 1):
                        curr = (past[0], i)
                        if curr in visited: loc, found = curr, True
                        else: visited.add(curr)
        else: # West
            if d[0] == 'R':
                ns += d[1]
                c_d = (c_d + 1) % 4
                if not found:
                    for i in range(past[0] + 1, ns + 1):
                        curr = (i, past[1])
                        if curr in visited: loc, found = curr, True
                        else: visited.add((i, past[1]))
            else:
                ns -= d[1]
                c_d = (c_d - 1) % 4
                if not found:
                    for i in range(ns, past[0]):
                        curr = (i, past[1])
                        if curr in visited: loc, found = curr, True
                        else: visited.add(curr)
    return (ns, ew), loc

def main():
    get_directions()
    blocks, loc = travel()
    print('Blocks:', abs(blocks[0]) + abs(blocks[1]))
    print('First:', abs(loc[0]) + abs(loc[1]))

if __name__ == "__main__":
    main()
