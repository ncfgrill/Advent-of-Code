'''
AoC 2023 day 2 parts 1 & 2
'''

from math import inf, prod

def check_line(line):
    block_numbers = {'red' : 12, 'green' : 13, 'blue' : 14}
    min_colors = {'red' : inf, 'green' : inf, 'blue' : inf}

    line = line.split(':')
    game_number = int((line[0]).split(' ')[1])
    line = line[1].split(';')

    for s in line:
        s = s.split(',')
        for b in s:
            b = (b.split(' '))
            value, color = int(b[-2]), b[-1].strip()
            if value > block_numbers[color]:
                game_number = 0
            if value > min_colors[color]:
                min_colors[color] = value

    return game_number, prod(list(min_colors.values()))

def read_input():
    total_sum, total_power = 0, 0

    with open('d02') as file:
        for line in file:
            temp_sum, temp_power = check_line(line)
            total_sum += temp_sum
            total_power += temp_power

    return total_sum, total_power

def main():
    t_sum, t_power = read_input()
    print('AoC 2023 Day 2\n  Part 1: {}\n  Part 2: {}'.format(t_sum, t_power))

if __name__ == '__main__':
    main()
