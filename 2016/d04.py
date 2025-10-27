'''
AoC 2016 Day 4 Parts 1 & 2
'''

from collections import Counter
from sys import argv

names = []

def get_names():
    global names

    with open(argv[1]) as f: names = f.readlines()
    for i, n in enumerate(names):
        names[i] = n.strip().split('[')
        names[i][-1] = names[i][-1].strip(']')
        names[i].append(int(names[i][0].split('-')[-1]))

def valid(freq, check):
    freq = [v[0] for v in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))]
    val = ''
    for c in freq[:5]: val += c

    return val == check

def convert(n):
    string, r, new = n[0], n[-1], ''
    for s in string:
        if s == '-': new += ' '
        else: new += chr((ord(s) - ord('a') + (r % 26)) % 26 + ord('a')) 

    if 'object' in new: return True

def count_letters():
    global names
    
    s, val, found = 0, 0, False
    for n in names:
        freq = dict(Counter([x for x in n[0] if not x.isnumeric()]))
        del freq['-']

        if valid(freq, n[1]): s += n[-1]
        if not found and convert(n): found, val = True, n[-1]
    return (s, val)

def main():
    get_names()
    sums = count_letters()
    print('Valid:', sums[0])
    print('Converted:', sums[1])

if __name__ == "__main__":
    main()
