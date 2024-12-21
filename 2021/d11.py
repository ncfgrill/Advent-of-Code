'''
AoC 2021 Day 11 parts 1 & 2
'''

grid = []

def get_grid():
    with open('d11') as f:
        for l in f:
            grid.append([int(x) for x in list(l.strip())])

def count_flashes():
    total_flashes, flashes = 0, -1

    while flashes != 0:
        flashes = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] > 9:
                    flashes += 1
                    grid[r][c] = 0
                    flash_so_inc_adjacent(r, c)
        total_flashes += flashes

    return total_flashes

def flash_so_inc_adjacent(r, c):
    upper = len(grid) - 1
    if r > 0:
        if c > 0:
            if grid[r-1][c-1] != 0:
                grid[r-1][c-1] += 1
        if grid[r-1][c] != 0:
            grid[r-1][c] += 1
        if c < upper:
            if grid[r-1][c+1] != 0:
                grid[r-1][c+1] += 1
    if r < upper:
        if c > 0:
            if grid[r+1][c-1] != 0:
                grid[r+1][c-1] += 1
        if grid[r+1][c] != 0:
            grid[r+1][c] += 1
        if c < upper:
            if grid[r+1][c+1] != 0:
                grid[r+1][c+1] += 1
    if c > 0:
        if grid[r][c-1] != 0:
            grid[r][c-1] += 1
    if c < upper:
        if grid[r][c+1] != 0:
            grid[r][c+1] += 1

def inc():
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1
    
    return count_flashes()

def sum_grid():
    return sum(map(sum, grid))

def  main():
    get_grid()
    total_flashes, steps, octo_sum = 0, 0, -1

    while octo_sum != 0:
        octo_sum = 0
        flashes = inc()
        if steps < 100:
            total_flashes += flashes
        octo_sum = sum_grid()
        steps += 1

    print('AoC \'21 - Day 11\n  P1: {}\n  P2: {}'.format(total_flashes, steps))

if __name__ == '__main__':
    main()
