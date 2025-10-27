'''
AoC 2015 Day 1 Parts 1 & 2
'''

from sys import argv

def main():
    floor, position, inc = 0, 0, 1
    with open(argv[1]) as f:
        for l in f:
            for d in l:
                position += inc
                if d == '(': floor += 1
                else:        floor -= 1

                if floor < 0: inc = 0
    
    print('Floor:', floor, '\nPosition:', position)

if __name__ == "__main__":
    main()
