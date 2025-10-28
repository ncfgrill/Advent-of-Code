'''
AoC 2020 Day 6 parts 1 & 2
'''

from sys import argv

def analyze(answers):
    u_answers, i_answers = set(), set()
    set_i = True

    for answer in answers:
        answer_set = set(answer)
        u_answers = u_answers.union(answer_set)
        if set_i:
            i_answers = answer_set
            set_i = False
        else:
            i_answers = i_answers.intersection(answer_set)

    return len(u_answers), len(i_answers)

def solve():
    answers = []
    u_total, i_total = 0, 0

    with open(argv[1]) as f:
        for line in f.readlines():
            if line == '\n':
                solution =  analyze(answers)
                u_total += solution[0]
                i_total += solution[1]
                answers.clear()
            else:
                answers.append(line.strip())

    solution = analyze(answers)
    u_total += solution[0]
    i_total += solution[1]

    return u_total, i_total

def main():
    solution = solve()
    print(f'AoC 2020 Day 6\nPart 1: {solution[0]}\nPart 2: {solution[1]}')

if __name__ == '__main__':
    main()
