'''
AoC 2020 Day 7 parts 1 & 2
'''

from sys import argv

BAGS = {}

class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = {}

def parse_line(line):
    name = f'{line[0]} {line[1]}'
    new_bag = Bag(name)

    i = 4
    while i < len(line):
        if line[i] == 'no':
            break

        if 'bag' in line[i]:
            new_bag.contains[f'{line[i-2]} {line[i-1]}'] = int(line[i-3])
        i += 1

    BAGS[name] = new_bag

def search(bag):
    if bag.name == 'shiny gold':
        return 1
    elif not len(bag.contains):
        return 0
    else:
        for i, sub_bag in enumerate(bag.contains):
            check = search(BAGS[sub_bag])
            if not check:
                if i == len(bag.contains):
                    return 0
            else:
                return check
        return 0

def count_inner(bags):
    total = 0

    for bag in bags.keys():
        total += bags[bag] * (count_inner(BAGS[bag].contains) + 1)

    return total

def solve():
    with open(argv[1]) as f:
        for line in f.readlines():
            parse_line(line.strip().split())

    total_contain = 0
    for bag in BAGS.keys():
        if bag == 'shiny gold':
            inner_bags = count_inner(BAGS[bag].contains)
        else:
            total_contain += search(BAGS[bag])

    return total_contain, inner_bags

def main():
    solution = solve()
    print(f'AoC 2020 Day 7\nPart 1: {solution[0]}\nPart 2: {solution[1]}')

if __name__ == '__main__':
    main()
