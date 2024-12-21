'''
AoC 2022 Day 5 parts 1 & 2
'''

from copy import deepcopy

crates = []
crates_2 = None
first_row_done = False

def construct(d):
    i = 1
    if d[i] == '1':
        return None

    while i < len(d):
        if not first_row_done:
            x = [d[i]] if d[i] != ' ' else []
            crates.append(x)
        else:
            if d[i] != ' ':
                crates[i//4].insert(0, d[i])
        i += 4

def move(d):
    i = d.strip().split(' ')
    num, s_f, s_t = int(i[1]), int(i[3]) - 1, int(i[5]) - 1
    len_c2 = len(crates_2[s_t])
    while num > 0:
        crates[s_t].append(crates[s_f].pop())
        crates_2[s_t].insert(len_c2 ,crates_2[s_f].pop())
        num -= 1

def top_stack():
    return ''.join([s[-1] for s in crates]), ''.join([s[-1] for s in crates_2])

def do_things():
    global first_row_done, crates_2

    time_to_move = False
    with open('d05') as f:
        for d in f.readlines():
            if d == '\n':
                crates_2 = deepcopy(crates)
                time_to_move = True
                continue
            if time_to_move:
                move(d)
            else:
                construct(d)
                first_row_done = True
    return top_stack()

def main():
    i, j = do_things()
    print('AoC \'22 - Day 5\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
