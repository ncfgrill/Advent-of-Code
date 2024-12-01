'''
AoC 2016 Day 10 Parts 1 & 2
'''

o_bin, instructions, bots, two_val = {}, {}, {}, set()

class Bot:
    def __init__(self, name, value):
        self.name, self.values = name, value

def get_bots_and_instructions():
    global instructions, bots, two_val

    with open('d10') as f: lines = f.readlines()
    for l in lines:
        l = l.strip().split(' ')
        if l[0] == 'bot':
            if l[1] not in bots: bots[l[1]] = Bot(l[1], [])
            instructions[l[1]] = {'l' : l[5:7], 'h' : l[10:]}
        else:
            b = l[-1]
            if b not in bots: bots[b] = Bot(b, [int(l[1])])
            else:
                bots[b].values.append(int(l[1]))
                if len(bots[b].values) == 2: two_val.add(b)

def execute(b):
    global two_val, bots, instructions, o_bin

    vals = [min(bots[b].values), max(bots[b].values)]
    insts = [instructions[b]['l'], instructions[b]['h']]

    for i, inst in enumerate(insts):
        if inst[0] == 'output': o_bin[int(inst[1])] = vals[i]
        else:
            bot = bots[inst[1]]
            bot.values.append(vals[i])
            if len(bot.values) == 2: two_val.add(bot.name)

def read_instructions():
    global bots, two_val

    bot = None
    while len(two_val) > 0:
        b = two_val.pop()
        if sorted(bots[b].values) == [17, 61]: bot = b
        execute(b)

    return bot

def main():
    global o_bin

    get_bots_and_instructions()
    print('Bot:', read_instructions())
    print('Prod:', o_bin[0] * o_bin[1] * o_bin[2])

if __name__ == "__main__":
    main()
