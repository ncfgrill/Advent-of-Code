'''
AoC 2015 Day 17 Parts 1 & 2
'''

containers, combs, min_c = [], 0, [99, 0]

def get_containers():
    global containers

    with open('d17') as f:
        containers = [int(l.strip()) for l in f.readlines()]

    containers.sort()
    containers.reverse()

def next_comb(t, i, n):
    global containers, combs, min_c

    if t == 150:
        combs += 1
        if n <= min_c[0]:
            if n < min_c[0]: min_c[0], min_c[1] = n, 1
            else: min_c[1] += 1

    elif t > 150: pass
    else:
        while i < len(containers):
            next_comb(t + containers[i], i + 1, n + 1)
            i += 1    

def main():
    global containers, combs, min_c
    
    get_containers()
    for i, c in enumerate(containers): next_comb(c, i + 1, 1)
    print('Combinations:', combs, '\nMin ways:', min_c[1])

if __name__ == "__main__":
    main()
