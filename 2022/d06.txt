'''
AoC 2022 Day 6 parts 1 & 2
'''

def read_signal():
    signals = []
    char_4 = 0
    l = 4

    with open('d06') as f:
        signal = f.readline()
    
    for i, s in enumerate(signal):
        if s in signals:
            j = None
            while j != s:
                j = signals.pop(0)
        signals.append(s)
        
        if len(signals) == l:
            if not char_4:
                char_4 = i + 1
                l = 14
            else:
                return char_4, i + 1

def main():
    i, j = read_signal()
    print('AoC \'22 - Day 6\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
