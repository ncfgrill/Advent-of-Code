'''
AoC 2020 Day 8 parts 1 & 2
'''

from sys import argv
from time import sleep

swapped = False

def get_arg(argument):
    sign, value = argument[0], int(argument[1:])
    flip = 1 if sign == '+' else -1

    return flip * value

def swap_op(op):
    global swapped

    if not swapped:
        if op == 'nop':
            op = 'jmp'
            swapped = True
        elif op == 'jmp':
            op = 'nop'
            swapped = True

    return op

def evaluate(instruction, swap=False):
    op = swap_op(instruction[0]) if swap else instruction[0]
    arg = get_arg(instruction[1])

    match op:
        case 'nop':
            return 0, 1
        case 'acc':
            return arg, 1
        case 'jmp':
            return 0, arg

def solve():
    global swapped

    with open(argv[1]) as f:
        instructions = f.readlines()

    acc1, acc2, i = 0, 0, 0
    executed = set()

    while True:
        if i in executed:
            break
        
        executed.add(i)
        values = evaluate(instructions[i].strip().split())
        acc1 += values[0]
        i += values[1]

    executed.clear()
    executed_save = set()
    i, i_save, acc_save = 0, 0, 0

    while i < len(instructions):
        if swapped:
            executed_save.add(i)
        else:
            i_save = i
            acc_save = acc2

        if i in executed:
            i = i_save
            acc2 = acc_save
            swapped = False

            for j in executed_save:
                executed.remove(j)
            executed_save.clear()
            values = evaluate(instructions[i].strip().split())
        else:
            values = evaluate(instructions[i].strip().split(), swap=True)
        
        executed.add(i)
        acc2 += values[0]
        i += values[1]

    return acc1, acc2

def main():
    solution = solve()
    print(f'AoC 2020 Day 7\nPart 1: {solution[0]}\nPart 2: {solution[1]}')

if __name__ == '__main__':
    main()
