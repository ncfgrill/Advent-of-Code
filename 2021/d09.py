'''
AoC 2021 Day 9 parts 1 & 2
'''

from sys import argv

network = []
points = []
valid = [x for x in range(1, 9)]
size = 0

def basin(p):
    global size

    r, c = p[0], p[1]
    network[r][c] = -1
    if r > 0 and network[r-1][c] in valid:
        size += 1
        basin((r-1, c))
    if r < len(network) - 1 and network[r+1][c] in valid:
        size += 1
        basin((r+1, c))
    if c > 0 and network[r][c-1] in valid:
        size += 1
        basin((r, c-1))
    if c < len(network[0]) - 1 and network[r][c+1] in valid:
        size += 1
        basin((r, c+1))

def find_basins():
    global size

    sizes = []
    for p in points:
        size = 1
        basin(p)
        sizes.append(size)
    m = 1
    for i in range(3):
        s = max(sizes)
        m *= s
        sizes[sizes.index(s)] = 0

    return m

def low_points():
    lp = 0

    with open(argv[1]) as f:
        l = None
        c = [int(a) for a in list(f.readline().strip())]
        n = [int(b) for b in list(f.readline().strip())]

        while True:
            network.append(c)
            for i in range(len(c)):
                comp = []
                if i != 0: comp.append(c[i-1])
                if i != len(c) - 1: comp.append(c[i+1])
                if l: comp.append(l[i])
                if n: comp.append(n[i])
                
                if min(comp) > c[i]:
                    lp += (1 + c[i])
                    points.append((len(network) - 1, i))

            if not n: break
            l, c = c, n
            n = [int(b) for b in list(f.readline().strip())]
  
    return lp, find_basins()

def main():
    i, j = low_points()
    print('AoC \'21 - Day 9\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
