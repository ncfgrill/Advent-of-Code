'''
AoC 2022 Day 3 parts 1 & 2
'''

from sys import argv

def get_priority(p):
    lower_case = ord('a') - 1
    upper_case = ord('A') - 27
    
    if p < ord('a'):
        return p - upper_case
    else:
        return  p - lower_case

def get_score():
    total_priority = 0

    group = 1
    grouping = {}
    group_priority = 0

    with open(argv[1]) as f:
        for d in f.readlines():
            ruck = {}
            mid = len(d.strip()) // 2
            index = 0
            found = False
           
            while index < mid:
                for i in range(0,2):
                    item = d[index + mid*i]
                    if item not in grouping and group == 1:
                        grouping[item] = group
                    elif item in grouping and grouping[item] == group - 1:
                        grouping[item] = group

                    if item not in ruck:
                        ruck[item] = i
                    elif ruck[item] != i and not found:
                        total_priority += get_priority(ord(item))
                        found = True
                index += 1
            group += 1
            
            if group == 4:
                g = grouping.items()
                g.sort(key=lambda x: x[1])
                group_priority += get_priority(ord(g[-1][0]))
                group = 1
                grouping = {}
        return total_priority, group_priority

def main():
    i, j = get_score()
    print('AoC \'22 - Day 3\n  P1: {}\n  P2: {}'.format(i, j))

if __name__ == '__main__':
    main()
