'''
AoC 2015 Day 6 Parts 1 & 2
'''

from sys import argv

grid_l = [[0 for i in range(1000)] for _ in range(1000)]
grid_b = [[0 for i in range(1000)] for _ in range(1000)]

def light_grid(l):
    global grid_l, grid_b
    
    l, i = l.split(' '), 2
    if len(l) == 4: i = 1
            
    c1, c2 = l[i].split(','), l[i+2].split(',')
    l1, l2, h1, h2 = int(c1[0]), int(c1[1]), int(c2[0]), int(c2[1])

    for j in range(l1, h1+1):
        for k in range(l2, h2+1):
            if i == 1:
                grid_l[j][k] = (grid_l[j][k] + 1) % 2
                grid_b[j][k] += 2
            elif l[1] == 'on':
                grid_l[j][k] = 1
                grid_b[j][k] += 1
            else:
                grid_l[j][k] = 0
                grid_b[j][k] = max(0, grid_b[j][k] - 1)

def main():
    global grid_l, grid_b

    with open(argv[1]) as f:
        for l in f:
            light_grid(l.strip())

    print('Lights:', sum(map(sum, grid_l)))
    print('Brightness:', sum(map(sum, grid_b)))

if __name__ == "__main__":
    main()
