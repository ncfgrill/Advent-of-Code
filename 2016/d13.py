'''
AoC 2016 Day 13 parts 1 & 2
'''

from sys import argv

min_steps, distinct = 99999999, set()

def is_wall(r, c):
    f_n = int(argv[1])

    v = r * r + 3 * r + 2 * r * c + c + c * c + f_n
    return bin(v)[2:].count('1') % 2 == 1

def next_step(r, c, visited, steps):
    global min_steps, distinct

    if steps <= 50: distinct.add((r, c))

    if steps > min_steps: return
    elif (r, c) == (31, 39): min_steps = min(min_steps, steps)
    else:
        if r - 1 >= 0:
            if (r - 1, c) not in visited and not is_wall(r - 1, c):
                v = visited.copy()
                v.add((r - 1, c))
                next_step(r - 1, c, v, steps + 1)
        if c - 1 >= 0:
            if (r, c - 1) not in visited and not is_wall(r, c - 1):
                v = visited.copy()
                v.add((r, c - 1))
                next_step(r, c - 1, v, steps + 1)
        if (r + 1, c) not in visited and not is_wall(r + 1, c):
            v = visited.copy()
            v.add((r + 1, c))
            next_step(r + 1, c, v, steps + 1)
        if (r, c + 1) not in visited and not is_wall(r, c + 1):
            v = visited.copy()
            v.add((r, c + 1))
            next_step(r, c + 1, v, steps + 1)

def main():
    next_step(1, 1, {(1,1)}, 0)
    print('Min steps:', min_steps)
    print('Distinct:', len(distinct))

if __name__ == "__main__":
    main()
