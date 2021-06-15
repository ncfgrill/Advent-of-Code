'''
AoC 2016 Day 3 Parts 1 & 2
'''

triangles = []

def get_triangles():
    global triangles

    with open('d03.txt') as f: triangles = f.readlines()
    for i, t in enumerate(triangles):
        triangles[i] = [int(x) for x in t.strip().split(' ') if len(x) > 0]

def check_triangles(t):
    return 1 if sum(t) > 2 * max(t) else 0

def check_cols():
    global triangles

    good = 0
    for c in range(len(triangles[0])):
        r = 0
        while r < len(triangles):
            t = [triangles[r][c], triangles[r+1][c], triangles[r+2][c]]
            if sum(t) > 2 * max(t): good += 1
            r += 3
    return good

def main():
    global triangles

    get_triangles()
    print('Valid (rows):', sum(map(check_triangles, triangles)))
    print('Valid (cols):', check_cols())

if __name__ == "__main__":
    main()
