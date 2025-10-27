'''
AoC 2015 Day 9 Parts 1 and 2
'''

from itertools import permutations
from sys import argv

graph = []

def create_graph():
    seen = set()
    with open(argv[1]) as f:
        i, s = -1, len(seen)

        for l in f.readlines():
            l = l.strip().split(' = ')
            cities = l[0].split(' to ')

            seen.add(cities[0])
            if len(seen) > s:
                i += 1
                s = len(seen)
                graph.append([])

                k = 0
                while k <= i:
                    graph[i].append(0)
                    k += 1

            graph[i].append(int(l[1]))

        for j in range(len(graph)):
            for k in range(j + 1, len(graph)):
                graph[k][j] = graph[j][k]

        graph.append([])
        l = len(graph)
        for i in range(l-1): graph[l-1].append(graph[i][l-1])
        graph[l-1].append(0)

def tsp(s):
    vert = [i for i in range(0, len(graph)) if i != s]

    min_path, max_path, perm = 99999999, 0, permutations(vert)
    for i in perm:
        dist, k = 0, s
        for j in i:
            dist += graph[k][j]
            k = j

        min_path, max_path = min(min_path, dist), max(max_path, dist)

    return (min_path, max_path)

def main():
    create_graph()
    min_d, max_d = 99999999, 0
    for s in range(0, len(graph)):
        d = tsp(s)
        min_d, max_d = min(min_d, d[0]), max(max_d, d[1])
    print('Shortest route:', min_d)
    print('Longest route:', max_d)

if __name__ == "__main__":
    main()
