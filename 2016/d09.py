'''
AoC 2016 Day 9 Parts 1 & 2
'''

def get_values(l, i, j):
    while l[j] != ')': j += 1
    v = l[i:j].split('x')
    return (int(v[0]), int(v[1])), j

def decompress(l, mul, ver):
    i, s = 0, 0
    while i < len(l):
        if l[i] == '(':
            v, j = get_values(l, i+1, i+4)
            if ver == 1: s += v[0] * v[1]
            else: s += decompress(l[j + 1 : j + 1 + v[0]], v[1] * mul, ver)
            i = j + v[0]
        else: s += mul
        i += 1
    return s

def main():
    with open('d09') as f: line = f.readline().strip()
    print('v1 decompression:', decompress(line, 1, 1))
    print('v2 decompression:', decompress(line, 1, 2))

if __name__ == "__main__":
    main()
