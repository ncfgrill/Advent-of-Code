'''
AoC 2017 Day 4 Parts 1 & 2
'''

from collections import Counter

def check(phrase):
    words = {}
    w, a = 1, 1

    for word in phrase.split():
        count = Counter(word)
        letters = sorted(count)
        freq_str = ''.join(l + str(count[l]) for l in letters)

        if freq_str in words:
            a = 0
            if word in words[freq_str]:
                w = 0
                break
            else:
                words[freq_str].add(word)
        else:
            words[freq_str] = {word}

    return w, a

def main():
    valid_words, valid_anagrams = 0, 0

    with open('d04') as f:
        for phrase in f.readlines():
            w, a = check(phrase.strip())
            valid_words += w
            valid_anagrams += a

    print('Part 1: {}'.format(valid_words))
    print('Part 2: {}'.format(valid_anagrams))

if __name__ == '__main__':
    main()
