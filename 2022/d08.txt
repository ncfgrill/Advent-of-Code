'''
AoC 2022 Day 8 parts 1 & 2
'''

trees = []

def get_trees():
    global trees

    with open('d08') as f:
        i = 0
        for d in f.readlines():
            trees.append([])
            for n in d:
                if n == '\n':
                    i += 1
                else:
                    trees[i].append(int(n))

def visible():
    rows = len(trees)
    cols = len(trees[0])
    visible = 0
    scenic = 0

    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                visible += 1
                continue

            t = trees[i][j]
            n, e, s, w = True, True, True, True
            d = 1
            v = False

            nv, ev, sv, wv = 0, 0, 0, 0

            while True:
                if n:
                    nv += 1
                    index = i - d
                    if t <= trees[index][j]:
                        n = False
                    else:
                        if index == 0:
                            if not v:
                                visible += 1
                            v = True
                            n = False
                if e:
                    ev += 1
                    index = j + d
                    if t <= trees[i][index]:
                        e = False
                    else:
                        if index == cols - 1:
                            if not v:
                                visible += 1
                            v = True
                            e = False
                if s:
                    index = i + d
                    sv += 1
                    if t <= trees[index][j]:
                        s = False
                    else:
                        if index == rows - 1:
                            if not v:
                                visible += 1
                            v = True
                            s = False
                if w:
                    index = j - d
                    wv += 1
                    if t <= trees[i][index]:
                        w = False
                    else:
                        if index == 0:
                            if not v:
                                visible += 1
                            v = True
                            w = False
                
                if not (n or e or s or w):
                    break
                d += 1
            s = nv * ev * sv * wv
            if s > scenic:
                scenic = s

    return visible, scenic

def main():
    get_trees()
    i, j = visible()
    print('AoC \'22 - Day 8\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
