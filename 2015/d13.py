'''
AoC 2015 Day 13 Parts 1 and 2
'''

from itertools import permutations

graph = []

def create_graph():
    seen = set()
    with open('d13') as f:
        i, s = -1, len(seen)

        for l in f.readlines():
            l = l.strip().split(' ')
            h = int(l[3]) if l[2] == 'gain' else -(int(l[3]))

            seen.add(l[0])
            if len(seen) > s:
                i += 1
                s = len(seen)
                graph.append([])

            graph[i].append(h)

        graph.append([0 for i in range(len(graph[0]))])
        for j in range(len(graph)):
            graph[j].insert(j, 0)
            graph[j].append(0)

def tsp(s, n):
    vert = [i for i in range(0, len(graph) - n) if i != s]

    min_path, max_path, perm = 99999999, 0, permutations(vert)
    for p in perm:
        h, k = 0, s
        for j in p:
            h += graph[k][j] + graph[j][k]
            k = j
        h += graph[k][s] + graph[s][k]
        
        min_path, max_path = min(min_path, h), max(max_path, h)

    return (min_path, max_path)

def find_seating(n):
    if n: create_graph()
    min_h, max_h = 99999999, 0
    for s in range(0, len(graph) - n):
        h = tsp(s, n)
        min_h, max_h = min(min_h, h[0]), max(max_h, h[1])
    print('Optimal happiness:', max_h)

def main():
    find_seating(1)
    find_seating(0)

if __name__ == "__main__":
    main()
