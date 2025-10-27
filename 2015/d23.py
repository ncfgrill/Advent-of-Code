'''
AoC 2015 Day 23 Parts 1 & 2
'''

from sys import argv

inst, a, b = [], 0, 0

def get_instructions():
    global inst

    with open(argv[1]) as f:
        inst = f.readlines()

    for i, d in enumerate(inst):
        inst[i] = d.strip().split(' ')
        if inst[i][0][0] == 'j':
            if inst[i][0][1] == 'i':
                inst[i][1] = inst[i][1].strip(',')
                inst[i][2] = int(inst[i][2])
            else: inst[i][1] = int(inst[i][1])

def execute(i):
    global inst, a, b

    if inst[i][0] == 'hlf':
        if inst[i][1] == 'a': a //= 2
        else:                 b //= 2
    elif inst[i][0] == 'tpl':
        if inst[i][1] == 'a': a *= 3
        else:                 b *= 3
    elif inst[i][0] == 'inc':
        if inst[i][1] == 'a': a += 1
        else:                 b += 1
    elif inst[i][0] == 'jmp':
        return i + inst[i][1]
    elif inst[i][0] == 'jie':
        if (inst[i][1] == 'a' and a % 2 == 0) or\
           (inst[i][1] == 'b' and b % 2 == 0):
            return i + inst[i][2]
    else: # inst[i][0] == 'jio'
        if (inst[i][1] == 'a' and a == 1) or\
           (inst[i][1] == 'b' and b == 1):
            return i + inst[i][2]

    return i + 1

def run():
    global inst, a, b

    i = 0
    while i < len(inst): i = execute(i)

    return b

def main():
    global a, b

    get_instructions()
    print('b if a = 0:', run())
    a, b = 1, 0
    print('b if a = 1:', run())

if __name__ == "__main__":
    main()
