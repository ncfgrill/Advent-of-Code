'''
AoC 2017 Day 7 Parts 1 & 2
'''

from sys import argv

registers = {}
a0, a1, a2, a4, a5, a6 = 0, 1, 2, 4, 5, 6
max_value = 0

def evaluate(args):
    global max_value
    r1, r2 = args[a0], args[a4]

    if r1 not in registers:
        registers[r1] = 0
    if r2 not in registers:
        registers[r2] = 0

    if eval(str(registers[r2]) + ' '.join(args[a5:a6+1])):
        value = int(args[a2])
        registers[r1] = registers[r1] + value \
                        if args[a1] == 'inc' \
                        else registers[r1] - value

        max_value = max(max_value, max(registers.values()))

def main():
    with open(argv[1]) as f:
        for line in f.readlines():
            evaluate(line.strip().split(' '))

    print(f'Day 1: {max(registers.values())}\nDay 2: {max_value}')

if __name__ == '__main__':
    main()
