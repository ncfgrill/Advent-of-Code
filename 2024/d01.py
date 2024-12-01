'''
AoC 2024 Day 1 Parts 1 & 2
'''

from math import abs
from time import sleep
from sys import maxint

def main():
    left, right, distance, big = [], [], 0, maxint
    with open('d01') as f:
        line = f.readline().split()
        left.add(int(line[0]))
        right.add(int(line[1]))
        
    for i in range(len(left)):
        min_left, min_right = min(left), min(right)
        distance += abs(min_left - min_right)
        left[left.index(min_left)], right[right.index(min_right)] = maxint, maxint
        
    print('Distance: {}'.format(distance))
    sleep(10)
    
if __name__ == '__main__':
    main()