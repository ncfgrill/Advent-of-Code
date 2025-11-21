'''
AoC Day 9 parts 1 & 2
'''

from sys import argv

preamble = []

def check_valid(num, i):
    lo = i - 25
    for p in preamble[lo : i]:
        if num - p in preamble:
            return True

    return False

def find_run(num):
    i, j = 0, 2

    while True:
        s = sum(preamble[i:j])
        if s < num:
            j += 1
        elif s > num:
            i += 1
        else:
            break
        
    return preamble[i : j]

def solve():
    invalid = None

    with open(argv[1]) as f:
        for i, num in enumerate(f.readlines()):
            num = int(num)
            if i >= 25:
                if not check_valid(num, i):
                    invalid = num
                    break
            preamble.append(num)

    num_run = find_run(invalid)
    return invalid, min(num_run) + max(num_run)

def main():
    solution = solve()
    print(f'AoC 2020 Day 9\nPart 1: {solution[0]}\nPart 2: {solution[1]}')

if __name__ == '__main__':
    main()
