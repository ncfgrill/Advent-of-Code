'''
AoC 2015 Day 2 Parts 1 & 2
'''

from sys import argv

def find_area(line):
    line = line.strip().split('x')
    l, w, h = int(line[0]), int(line[1]), int(line[2])
            
    a1, a2, a3 = l*w, w*h, h*l 
    p1 = min(l, w)
    if p1 == w: p2 = min(l, h)
    else:       p2 = min(w, h)

    return (2*(a1 + a2 + a3) + min(a1, a2, a3), 2*(p1 + p2) + l*w*h)

def main():
    with open(argv[1]) as f:
        lines = f.readlines()
        a = map(find_area, lines)
        a = [sum(x) for x in zip(*list(a))]

        print('Area: ' + str(a[0]) + '\nRibbon: ' + str(a[1]))

if __name__ == "__main__":
    main()
