'''
AoC 2024 Day 1 Parts 1 & 2
'''

from sys import argv

MAX_INT = 999999999

def main():
    left_l, right_l = [], []
    right_d = {}
    distance, similarity = 0, 0
    with open(argv[1]) as f:
        for line in f.readlines():
            left_v, right_v = [int(x) for x in line.split()]
            
            left_l.append(left_v)
            right_l.append(right_v)
                
            if right_v in right_d:
                right_d[right_v] = right_d[right_v] + 1
            else:
                right_d[right_v] = 1
        
    for i in range(len(left_l)):
        min_left, min_right = min(left_l), min(right_l)
        distance += abs(min_left - min_right)
        
        try:
            similarity += left_l[left_l.index(min_left)] * right_d[left_l[left_l.index(min_left)]]
        except:
            pass
        
        left_l[left_l.index(min_left)], right_l[right_l.index(min_right)] = MAX_INT, MAX_INT
    
    print('Part 1: {}'.format(distance))
    print('Part 2: {}'.format(similarity))
    
if __name__ == '__main__':
    main()
