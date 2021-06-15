'''
AoC 2015 Day 7 Parts 1 & 2
'''

signals, values = {}, {}

def get_signals_and_values():
    with open('d07') as f:
        for l in f:
            l = l.strip('\n').split('->')
            try: values[l[1].strip()] = int(l[0].strip())
            except ValueError: signals[l[1].strip()] = l[0].strip().split(' ')

def find_a():
    while 'a' not in values:
        for sig in list(signals.items()):
            if 'AND' in sig[1]:
                if sig[1][0] in '0123456789' and sig[1][2] in values:
                    values[sig[0]] = int(sig[1][0]) & values[sig[1][2]]
                elif sig[1][0] in values and  sig[1][2] in '0123456789':
                    values[sig[0]] = values[sig[1][0]] & int(sig[1][2])
                elif sig[1][0] in values and sig[1][2] in values:
                    values[sig[0]] = values[sig[1][0]] & values[sig[1][2]]
            elif 'OR' in sig[1]:
                if sig[1][0] in '0123456789' and sig[1][2] in values:
                    values[sig[0]] = int(sig[1][0]) | values[sig[1][2]]
                elif sig[1][0] in values and sig[1][2] in '0123456789':
                    values[sig[0]] = values[sig[1][0]] | int(sig[1][2])
                elif (sig[1][0] in values) and (sig[1][2] in values):
                    values[sig[0]] = values[sig[1][0]] | values[sig[1][2]]
            elif 'NOT' in sig[1]:
                if sig[1][1] in values:
                    values[sig[0]] = ~values[sig[1][1]]
            elif 'LSHIFT' in sig[1]:
                if sig[1][0] in values:
                    values[sig[0]] = values[sig[1][0]] << int(sig[1][2])
            elif 'RSHIFT' in sig[1]:
                if sig[1][0] in values:
                    values[sig[0]] = values[sig[1][0]] >> int(sig[1][2])
            else:
                if len(sig[1]) == 1 and sig[1][0] in values:
                    values[sig[0]] = values[sig[1][0]]

def main():
    global signals, values

    get_signals_and_values()
    find_a()
    print('a =', values['a'])

    save = values['a']
    signals, values = {}, {}
    get_signals_and_values()
    values['b'] = save
    find_a()

    print('a =', values['a'])

if __name__ == "__main__":
    main()
