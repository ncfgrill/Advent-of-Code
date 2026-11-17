'''
AoC 2017 Day 12 Parts 1 & 2
'''

from sys import argv

nodes = {}
zero_total = 0
group_total = 1

class Node:
    def __init__(self, value):
        self.value = value
        self.connectors = set()
        self.visited = False

def make_graph(args):
    value = int(args[0])
    connections = [int(c) for c in args[2].strip().split(',')]
    
    if value not in nodes:
        nodes[value] = Node(value)

    for c in connections:
        if c not in nodes:
            nodes[c] = Node(c)
        nodes[value].connectors.add(nodes[c])

def traverse_graph(node, inc_zero=False):
    global zero_total    

    if node.visited:
        return

    if inc_zero:
        zero_total += 1
    node.visited = True

    for c in node.connectors:
        if not c.visited:
            traverse_graph(c, inc_zero)

def main():
    global zero_total, group_total

    with open(argv[1]) as f:
        for line in f.readlines():
            make_graph(line.split(sep=' ', maxsplit=2))

    traverse_graph(nodes[0], True)
    for node in nodes:
        if not nodes[node].visited:
            traverse_graph(nodes[node])
            group_total += 1

    print(f'Day 1: {zero_total}\nDay 2: {group_total}')

if __name__ == '__main__':
    main()
