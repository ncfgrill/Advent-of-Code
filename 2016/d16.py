'''
AoC 2016 Day 16 parts 1 & 2
'''

from sys import argv

def replace(state):
    return state.replace('1', '2').replace('0', '1').replace('2', '0')

def check_sum(state):
    cs, i, r = '', 0, {'11' : '1', '00' : '1', '10' : '0', '01' : '0'}

    while i < len(state):
        cs += r[state[i:i+2]]
        i += 2

    return cs if len(cs) % 2 != 0 else check_sum(cs)

def fill(state, l):
    while len(state) < l: state += '0' + replace(state[::-1])
    return state[:l]

def main():
    initial = argv[1]
    print('CS 272:', check_sum(fill(initial, 272)))
    print('CS 35651584', check_sum(fill(initial, 35651584)))

if __name__ == "__main__":
    main()
