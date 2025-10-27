'''
AoC 2016 Day 18 parts 1 & 2
'''

from sys import argv

def get_floor():
    with open(argv[1]) as f: return [f.readline().strip()]

def count(floor):
    return sum(1 if c == '.' else 0 for c in floor)

def find_safe(floors):
    i, s1 = 1, None

    while i < 400000:
        if i == 40: s1 = sum(map(count, floors))
        floors.append('')
        f, j, l = floors[i-1], 0, len(floors[0])
        while j < l:
            if j == 0:
                if f[:j+2] in ('^^', '.^'): floors[i] += '^'
                else: floors[i] += '.'
            elif j == l - 1:
                if f[j-1:j+1] in ('^^', '^.'): floors[i] += '^'
                else: floors[i] += '.'
            else:
                if f[j-1:j+2] in ('^^.', '^..', '.^^', '..^'): floors[i] += '^'
                else: floors[i] += '.'
            j += 1
        i += 1

    return (s1, sum(map(count, floors)))

def main():
    s = find_safe(get_floor())
    print('Safe (40):', s[0], '\nSafe (400000):', s[1])

if __name__ == "__main__":
    main()
