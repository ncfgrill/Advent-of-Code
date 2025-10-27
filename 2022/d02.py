'''
AoC 2022 Day 2 parts 1 & 2
'''

from sys import argv

def get_score():
    rounds = []
    total_score = 0
    total_real_score = 0

    with open(argv[1]) as f:
        for d in f.readlines():
            r = d.strip().split(' ')
            opp, you = r[0], r[1]
            score = 0
            real_score = 0

            if opp == 'A':
                if you == 'X':
                    score += 4
                    real_score += 3
                elif you == 'Y':
                    score += 8
                    real_score += 4
                else:
                    score += 3
                    real_score += 8
            elif opp == 'B':
                if you == 'X':
                    score += 1
                    real_score += 1
                elif you == 'Y':
                    score += 5
                    real_score += 5
                else:
                    score += 9
                    real_score += 9
            else:
                if you == 'X':
                    score += 7
                    real_score += 2
                elif you == 'Y':
                    score += 2
                    real_score += 6
                else:
                    score += 6
                    real_score = 7
            total_score += score
            total_real_score += real_score

    return total_score, total_real_score

def main():
    i, j = get_score()
    print('AoC \'22 - Day 2\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
