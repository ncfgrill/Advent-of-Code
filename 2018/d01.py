'''
AoC 2018 Day 1 Parts 1 & 2
'''

from sys import argv

def check_freqs(freqs):
    seen = { 0 }
    freq = i = 0
    n_freqs = len(freqs)

    while True:
        freq += freqs[i % n_freqs]
        if freq in seen:
            return sum(freqs), freq
        else:
            seen.add(freq)
        i += 1

def main():
    with open(argv[1]) as f:
        ans = check_freqs([int(x) for x in f.readlines()])

    print(f'Day 1: {ans[0]}\nDay 2: {ans[1]}')

if __name__ == '__main__':
    main()
