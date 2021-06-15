'''
AoC 2016 Day 2 Parts 1 and 2
'''

instructions = []

def get_instructions():
    global instructions

    with open('d02.txt') as f: instructions = f.readlines()
    for i, l in enumerate(instructions): instructions[i] = l.strip()

def find_code():
    global instructions

    keypad1 = [['1','2','3'],
               ['4','5','6'],
               ['7','8','9']]
    keypad2 = [['x','x','1','x','x'],
               ['x','2','3','4','x'],
               ['5','6','7','8','9'],
               ['x','A','B','C','x'],
               ['x','x','D','x','x']]
    pos1, pos2, code1, code2 = [1, 1], [2, 0], '', ''

    for i in instructions:
        for d in i:
            if d == 'U':
                if pos1[0] > 0: pos1[0] -= 1
                if pos2[0] > 0 and keypad2[pos2[0] - 1][pos2[1]] != 'x':
                    pos2[0] -= 1
            elif d == 'R':
                if pos1[1] < 2: pos1[1] += 1
                if pos2[1] < 4 and keypad2[pos2[0]][pos2[1] + 1] != 'x':
                    pos2[1] += 1
            elif d == 'D':
                if pos1[0] < 2: pos1[0] += 1
                if pos2[0] < 4 and keypad2[pos2[0] + 1][pos2[1]] != 'x':
                    pos2[0] += 1
            else: # d == 'L':
                if pos1[1] > 0: pos1[1] -= 1
                if pos2[1] > 0 and keypad2[pos2[0]][pos2[1] - 1] != 'x':
                    pos2[1] -= 1

        code1 += keypad1[pos1[0]][pos1[1]]
        code2 += keypad2[pos2[0]][pos2[1]]
    return code1, code2

def main():
    get_instructions()
    codes = find_code()
    print('Easy code:', codes[0])
    print('Hard code:', codes[1])

if __name__ == "__main__":
    main()
