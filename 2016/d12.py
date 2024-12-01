'''
AoC 2016 Day 12 parts 1 & 2
'''

def get_instructions():
    with open('d12') as f: insts = f.readlines()
    return [i.strip().split(' ') for i in insts]

def execute_instructions(c):
    reg, insts, i = {'a' : 0, 'b' : 0, 'c' : c, 'd' : 0}, get_instructions(), 0

    while i < len(insts):
        inst = insts[i]
        if inst[0] == 'cpy':
            reg[inst[2]] = int(inst[1]) if inst[1].isnumeric() else reg[inst[1]]
        elif inst[0] == 'inc': reg[inst[1]] += 1
        elif inst[0] == 'dec': reg[inst[1]] -= 1
        else:
            v = int(inst[1]) if inst[1].isnumeric() else reg[inst[1]]
            if v != 0: i += int(inst[2]) - 1
        i += 1
    return reg['a']

def main():
    print('Reg a (0):', execute_instructions(0))
    print('Reg a (1):', execute_instructions(1))

if __name__ == "__main__":
    main()
