'''
AoC 2021 Day 10 parts 1 & 2
'''

def find_mid(im):
    return sorted(im)[len(im)//2]

def find():
    cor_pts = {
                ')' : 3,
                ']' : 57,
                '}' : 1197,
                '>' : 25137
              }
    inc_pts = {
                ')' : 1,
                ']' : 2,
                '}' : 3,
                '>' : 4
              }

    cm, im = 0, []
    opn, cls = '([{<', ')]}>'

    with open('d10') as f:
        line = f.readline().strip()
        while line:
            i, save, cor = 0, [], False
            while i < len(line):
                c = line[i]
                if c in opn:
                    save.append(cls[opn.index(c)])
                else:
                    if cls.index(c) != cls.index(save[-1]):
                        cm += cor_pts[c]
                        cor = True
                        break
                    else:
                        save.pop(-1)
                i += 1
            if not cor:
                score = 0
                for s in reversed(save):
                    score *= 5
                    score += inc_pts[s]
                im.append(score)

            line = f.readline().strip()
    return cm, find_mid(im)

def main():
    i, j = find()
    print('AoC \'21 - Day 10\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
