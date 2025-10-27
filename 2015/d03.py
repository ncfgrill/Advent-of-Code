'''
AoC 2015 Day 3 Parts 1 & 2
'''

from sys import argv

v1, h1, v2, h2, v3, h3, turn = 0, 0, 0, 0, 0, 0, 0

def num_presents(d):
    global v1, h1, v2, h2, v3, h3, turn

    turn += 1
    if d == '^':
        v1 += 1
        if turn % 2 == 1: v2 += 1
        else:             v3 += 1
    elif d == 'v':
        v1 -= 1
        if turn % 2 == 1: v2 -= 1
        else:             v3 -= 1
    elif d == '>':
        h1 += 1
        if turn % 2 == 1: h2 += 1
        else:             h3 += 1
    else:
        h1 -= 1
        if turn % 2 == 1: h2 -= 1
        else:             h3 -= 1
    
    return ((v1, h1), (v2, h2), (0, 0)) if turn % 2 == 1 else ((v1, h1), (0, 0), (v3, h3))

def main():
    with open(argv[1]) as f:
        lines = [l.strip() for l in f.readline()]
        houses = map(num_presents, lines)
        houses = list(houses)
        houses.append(((0,0), (0,0), (0,0))) # account for starting location
        
        santa = set([trip[1] for trip in houses])
        robo_santa = set([trip[2] for trip in houses])
        houses = set([trip[0] for trip in houses])

        print('Santa: ' + str(len(houses)) +\
              '\nSanta and Robo: ' +\
              str(len(santa) + len(robo_santa.difference(santa))))

if __name__ == "__main__":
    main()
