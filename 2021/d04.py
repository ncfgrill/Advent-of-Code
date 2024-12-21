'''
AoC 2021 Day 4 parts 1 & 2
'''

boards = []
b_num = 1

def get_info():
    with open('d04') as f:
        nums = [int(n) for n in f.readline().split(',')]
        l = f.readline()
        while l:
            boards.append([[[int(x) for x in next(f).split()] for y in range(5)], 0, 0])
            l = f.readline()
    return nums

def check_bingo(b):
    for i in range(len(b)):
        if b[i][0] == b[i][1] == b[i][2] == b[i][3] == b[i][4] == -1:
            return True
        if b[0][i] == b[1][i] == b[2][i] == b[3][i] == b[4][i] == -1:
            return True
    return False

def check_boards(n):
    global b_num

    for board in boards:
        if board[1] != 0: continue
        b = board[0]
        for r in range(len(b)):
            for i in range(len(b[r])):
                if b[r][i] == n:
                    b[r][i] = -1
                    if check_bingo(b):
                        board[1] = b_num
                        board[2] = n
                        b_num += 1

def get_score(game):
    unmarked = 0
    for x in game[0]:
        for y in x:
            if y != -1: unmarked += y

    return unmarked * game[2]

def get_boards():
    global boards
    l = sorted(boards, key=lambda x: x[1])
    return get_score(l[0]), get_score(l[-1])

def bingo():
    nums = get_info()
    first, save = False, None
    s1, s2 = None, None
    for n in nums:
        check_boards(n)

    return get_boards()

def main():
    first, last = bingo()
    print('AoC \'21 - Day 4\n  P1: {}\n  P2: {}'.format(first, last))

if __name__ == '__main__':
    main()
