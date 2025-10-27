'''
AoC 2016 Day 21 parts 1 & 2
'''

from sys import argv

code, insts = ['a','b','c','d','e','f','g','h'], None

def get_instructions():
    global insts

    with open(argv[1]) as f:
        insts = [l.strip().split(' ') for l in f.readlines()]

def swp(i):
    global code

    p = (int(i[2]), int(i[5])) if i[1] == 'position' else\
        (code.index(i[2]), code.index(i[5]))
    code[p[0]], code[p[1]] = code[p[1]], code[p[0]]

def rot(i, u = False):
    global code

    if i[1] == 'based':
        index = code.index(i[-1]) + 1
        if not u:
            if index > 4: index += 1
        else:
            conv = {0 : 1, 1 : 1, 2 : -2, 3 : 2, 4 : -1, 5 : 3, 6 : 0, 7 : 4}
            index -= 1
            index = -conv[index]
        code = code[-index:] + code[:-index]
    else:
        index = int(i[2]) if i[1] == 'left' else -int(i[2])
        if u: index = -index
        code = code[index:] + code[:index]

def rev(i):
    global code

    i1, i2 = int(i[2]), int(i[4]) + 1
    code = code[:i1] + list(reversed(code[i1:i2])) + code[i2:]

def mov(i, u = False):
    global code

    rem = code[int(i[2])] if not u else code[int(i[5])]
    ins = int(i[5]) if not u else int(i[2])
    code.remove(rem)
    code.insert(ins, rem)

def scramble():
    global code, insts

    for i in insts:
        if i[0] == 'swap': swp(i)
        elif i[0] == 'rotate': rot(i)
        elif i[0] == 'reverse': rev(i)
        else: mov(i)
    return ''.join(c for c in code)

def unscramble():
    global code, insts

    code, index = ['f','b','g','d','c','e','a','h'], len(insts) - 1
    while index >= 0:
        i = insts[index]
        if i[0] == 'swap': swp(i)
        elif i[0] == 'rotate': rot(i, True)
        elif i[0] == 'reverse': rev(i)
        else: mov(i, True)
        index -= 1
    return ''.join(c for c in code)

def main():
    get_instructions()
    print('Scrambled:', scramble())
    print('Unscrambled:', unscramble())

if __name__ == '__main__':
    main()
