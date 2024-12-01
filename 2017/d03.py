'''
AoC 2017 Day 3 Parts 1 & 2
'''

value = 289326
sq_values = {(0,0) : 1}
sq_check = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]

def manhattan():
    start, x, y = 1, 0, 0
    directions, index = ['r', 'u', 'l', 'd'], 0
    d, step = directions[index], 1
    stop, change = 1, 0

    larger = 0

    while start < value:
        if d == 'r':
            x += 1
        elif d == 'u':
            y += 1
        elif d == 'l':
            x -= 1
        else: # direction == 'd'
            y -= 1

        if larger < value:
            larger = create(x, y)

        start += 1

        if step == stop:
            index = (index + 1) % len(directions)
            d = directions[index]
            step = 1

            if change:
                stop += 1
                change = 0
            else:
                change = 1
        else:
            step += 1

    return abs(x) + abs(y), larger

def create(x, y):
    sq_sum = 0

    for t in sq_check:
        try:
            sq_sum += sq_values[(x + t[0], y + t[1])]
        except:
            continue

    sq_values[(x, y)] = sq_sum
    return sq_sum

def main():
    man, larger = manhattan()
    print('Part 1: {}'.format(man))
    print('Part 2: {}'.format(larger))

if __name__ == '__main__':
    main()
