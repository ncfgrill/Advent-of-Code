'''
AoC 2020 Day 1 parts 1 & 2
'''

from sys import argv

def solve():
    with open(argv[1]) as f:
        num_list = [int(i) for i in f.readlines()]
        
    p1_done, p2_done = False, False
    p1_sol, p2_sol = None, None

    for i, num_1 in enumerate(num_list):
        check = 2020 - num_1
        if not p1_done and check in num_list:
            p1_sol = num_1 * check
            p1_done = True

        j = i+1
        while j < len(num_list):
            num_2 = num_list[j]
            check = 2020 - num_1 - num_2
            if not p2_done and check in num_list:
                p2_sol = num_1 * num_2 * check
                p2_done = True
            j += 1

        if p1_done and p2_done: break

    return p1_sol, p2_sol 

def main():
    solution = solve()
    print(f'AoC 2020 Day 1\nPart 1: {solution[0]}\nPart 2: {solution[1]}')

if __name__ == '__main__':
    main()
