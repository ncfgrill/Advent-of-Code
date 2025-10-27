'''
AoC 2017 Day 6 Parts 1 & 2
'''

from sys import argv

mem_blocks = None
configs = set()
find_again = None

def find_max():
    size_max, i_max = 0, None

    for i, n in enumerate(mem_blocks):
        if n > size_max:
            size_max, i_max = n, i

    return i_max

def add_config():
    global find_again

    config = '_'.join(str(b) for b in mem_blocks)

    if not find_again:
        if config in configs:
            find_again = config
            return False

        configs.add(config)
    else:
        if config == find_again:
            return False
    
    return True

def new_cycle():
    i = find_max()

    value = mem_blocks[i]
    mem_blocks[i] = 0

    while value > 0:
        i = (i + 1) % len(mem_blocks)
        mem_blocks[i] += 1
        value -= 1

    return add_config()

def main():
    global mem_blocks

    with open(argv[1]) as f:
        mem_blocks = [int(n) for n in f.readline().split()]

    add_config()
    cycles = 1
    again = 1

    while new_cycle():
        cycles += 1

    while new_cycle():
        again += 1

    print('Part 1: {}'.format(cycles))
    print('Part 2: {}'.format(again))

if __name__ == '__main__':
    main()
