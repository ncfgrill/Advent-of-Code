'''
AoC 2016 Day 8 Parts 1 & 2
'''

from sys import argv

pad = [[' ' for i in range(50)] for _ in range(6)]

def get_instructions():
    with open(argv[1]) as f: lines = f.readlines()
    return [l.strip().split(' ') for l in lines]

def rect(rc):
    global pad

    for r in range(rc[1]):
        for c in range(rc[0]): pad[r][c] = '\u2588'

def row(r, v):
    global pad

    new, l = pad[r].copy(), len(pad[r])
    for i in range(l): new[(i + v) % l] = pad[r][i]
    pad[r] = new

def col(c, v):
    global pad

    save, l = [pad[x][c] for x in range(len(pad))], len(pad)
    for i in range(l): pad[(i + v) % l][c] = save[i]

def sum_screen(l):
    return sum([0 if v == ' ' else 1 for v in l])


def execute_instructions():
    for i in get_instructions():
        if i[0] == 'rect': rect([int(n) for n in i[1].split('x')])
        elif i[1] == 'row': row(int((i[2].split('='))[1]), int(i[4]))
        else: col(int((i[2].split('='))[1]), int(i[4]))

def main():
    global pad

    execute_instructions()
    print('Pixels:', sum(map(sum_screen, pad)), '\nDisplay')
    for p in pad: print(''.join(str(c) for c in p))

if __name__ == "__main__":
    main()
