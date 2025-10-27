'''
AoC 2015 Day 18 Parts 1 & 2
'''

from copy import deepcopy as dc
from sys import argv

grid_1, grid_2, corners = [[0 for i in range(100)]], [], []

def create_initial_grid():
    global grid_1, grid_2, corners

    with open(argv[1]) as f:
        for l in f.readlines():
            grid_1.append([1 if i == '#' else 0 for i in l.strip()])

    grid_1.append([0 for i in range(100)])
    for l in grid_1:
        l.insert(0, 0)
        l.append(0)

    grid_2 = dc(grid_1)
    corners = [(1, 1),
               (1, len(grid_1) - 2),
               (len(grid_1) - 2, 1),
               (len(grid_1) - 2, len(grid_1) - 2)]

    for p in corners: grid_2[p[0]][p[1]] = 1

def modify_grid():
    global grid_1, grid_2, corners
    
    gc1, gc2 = dc(grid_1), dc(grid_2)

    for i in range(1, len(grid_1) - 1):
        for j in range(1, len(grid_1[i]) - 1):
            s1 = grid_1[i-1][j-1] + grid_1[i-1][j] + grid_1[i-1][j+1] +\
                 grid_1[i][j-1] + grid_1[i][j+1] +\
                 grid_1[i+1][j-1] + grid_1[i+1][j] + grid_1[i+1][j+1]
    
            if (i, j) not in corners:
                s2 = grid_2[i-1][j-1] + grid_2[i-1][j] + grid_2[i-1][j+1] +\
                     grid_2[i][j-1] + grid_2[i][j+1] +\
                     grid_2[i+1][j-1] + grid_2[i+1][j] + grid_2[i+1][j+1]
            else: s2 = -1

            if gc1[i][j] == 1:
                if s1 < 2 or s1 > 3: gc1[i][j] = 0
            else:
                if s1 == 3: gc1[i][j] = 1

            if s2 != -1:
                if gc2[i][j] == 1:
                    if s2 < 2 or s2 > 3: gc2[i][j] = 0
                else:
                    if s2 == 3: gc2[i][j] = 1

    grid_1, grid_2 = gc1, gc2

def main():
    global grid_1, grid_2

    create_initial_grid()
    i = 0

    while i < 100:
        modify_grid()
        i += 1

    s1, s2 = sum(map(sum, grid_1)), sum(map(sum, grid_2))
    print('Grid:', s1, '\nBroken grid:', s2)

if __name__ == "__main__":
    main()
