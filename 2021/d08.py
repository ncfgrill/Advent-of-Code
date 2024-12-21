'''
AoC 2021 Day 8 parts 1 & 2
'''

def check_output():
    unique = 0
    with open('d08') as f:
        output = f.readline().strip()
        while output:
            output = output.split(' | ')[1].split()
            for o in output:
                if len(o) in [2, 3, 4, 7]: unique += 1

            output = f.readline().strip()
    return unique, None

def main():
    i, j = check_output()
    print('AoC \'21 - Day 8\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
