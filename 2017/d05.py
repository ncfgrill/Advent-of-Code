'''
AoC 2017 Day 5 Parts 1 & 2
'''

from sys import argv

def main():
    num_1, num_2, index = 0, 0, 0
    steps_1, steps_2 = [], []

    with open(argv[1]) as f:
        for line in f.readlines():
            steps_1.append(int(line))
            steps_2.append(int(line))

    while index >= 0 and index < len(steps_1):
        num_1 += 1
        temp = steps_1[index]
        steps_1[index] += 1
        index += temp

    index = 0
    while index >= 0 and index < len(steps_2):
        num_2 += 1
        temp = steps_2[index]

        if temp >= 3:
            steps_2[index] -= 1
        else:
            steps_2[index] += 1

        index += temp

    print('Part 1: {}'.format(num_1))
    print('Part 2: {}'.format(num_2))

if __name__ == '__main__':
    main()
