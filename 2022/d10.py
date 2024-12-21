'''
AoC 2022 Day 10 parts 1 & 2
'''

screen = ['#']

def print_screen():
    for i in range(len(screen)):
        if not (i % 40):
            print('')
        print(screen[i], end='')

def signals():
    cycle = 1
    x = 1
    total = 0

    with open('d10') as f:
        for d in f.readlines():
            a = d.strip().split(' ')
            if a[0] == 'addx':
                if cycle % 40 in range(x - 1, x + 2):
                    screen.append('#')
                else:
                    screen.append(' ')
                cycle += 1
                if not (cycle % 20) and ((cycle / 20) % 2):
                    if cycle <= 220:
                        total += cycle * x
                x += int(a[1])
            if cycle % 40 in range(x - 1, x + 2):
                screen.append('#')
            else:
                screen.append(' ')
            cycle += 1
            if not (cycle % 20) and ((cycle / 20) % 2):
                if cycle <= 220:
                    total += cycle * x
    return total

def main():
    i = signals()
    print('AoC \'22 - Day 10\n  P1: {}\n  P2:'.format(i))
    print_screen()

if __name__ == '__main__':
    main()
