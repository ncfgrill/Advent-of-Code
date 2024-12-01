'''
AoC 2016 Day 6 Parts 1 & 2
'''

from collections import Counter

cols = []

def get_cols():
    global cols

    with open('d06') as f: lines = f.readlines()

    lines = [l.strip() for l in lines]
    cols = ['' for x in lines[0]]
    
    for l in lines:
        for i, c in enumerate(l): cols[i] += c

def col_freq():
    global cols

    m1, m2 = '', ''
    for c in cols:
        s = list(sorted(dict(Counter(c)).items(), key=lambda kv: kv[1]))
        m1 += s[-1][0]
        m2 += s[0][0]
    return (m1, m2)

def main():
    get_cols()
    m = col_freq()
    print('Message (most):', m[0], '\nMessage (least):', m[1])

if __name__ == "__main__":
    main()
