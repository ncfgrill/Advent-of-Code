'''
AoC 2015 Day 10 Parts 1 and 2
'''

def main():
    string, i = '1113122113', 0

    while i < 50:
        if i == 40: print('Length:', len(string))
        new, curr, freq = '', string[0], 1

        for j in range(1, len(string)):
            if string[j] == curr: freq += 1
            else:
                new += str(freq) + curr
                curr, freq = string[j], 1

        string = new + str(freq) + curr
        i += 1

    print('Length:', len(string))

if __name__ == '__main__':
    main()
