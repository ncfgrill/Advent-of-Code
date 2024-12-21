'''
AoC 2023 Day 1 parts 1 & 2
'''

words = {
         'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5,
         'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9
        }

def read_input():
    total_1, total_2 = 0, 0
    with open('d01') as file:
        for line in file:
            total_1 += read_number_calibration(line)
            total_2 += read_word_calibration(line)
    
    return total_1, total_2

def read_number_calibration(line):
    first = 'x'
    i = 0
    while not first.isdigit():
        first = line[i]
        i += 1

    last = 'x'
    i = -1
    while not last.isdigit():
        last = line[i]
        i -= 1

    return int(first + last)

def read_word_calibration(line):
    global words
    length = len(line)

    first = None
    i = 0
    while True:
        first = line[i]
        if first.isdigit():
            break
        else:
            if first in 'fenost':
                if i + 3 < length and line[i:i+3] in words:
                    first = words[line[i:i+3]]
                    break
                if i + 4 < length and line[i:i+4] in words:
                    first = words[line[i:i+4]]
                    break
                if i + 5 < length and line[i:i+5] in words:
                    first = words[line[i:i+5]]
                    break
        i += 1

    last = None
    i = -1
    while True:
        last = line[i]
        if last.isdigit():
            break
        else:
            if last in 'fenost':
                if i < -2 and line[length+i:length+i+3] in words:
                    last = words[line[length+i:length+i+3]]
                    break
                if i < -3  and line[length+i:length+i+4] in words:
                    last = words[line[length+i:length+i+4]]
                    break
                if i + 5 < length and line[length+i:length+i+5] in words:
                    last = words[line[length+i:length+i+5]]
                    break
        i -= 1

    return int(str(first) + str(last))

def main():
    p1, p2 = read_input()
    print('AoC Day 1\n  Part 1: {}\n  Part 2: {}'.format(p1, p2))

if __name__ == '__main__':
    main()
