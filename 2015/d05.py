'''
AoC 2015 Day 5 Parts 1 & 2
'''

def nice_strings(line):
    nice_str = [0, 0]
    line = line.strip()

    # Part 1
    forbid = ['ab', 'cd', 'pq', 'xy']

    i, end = 0, len(line) - 1
    nice, vow, dub = True, 0, False

    while i < end:
        if line[i] in 'aeiou':               vow += 1
        if not dub and line[i] == line[i+1]: dub = True
        if line[i:i+2] in forbid:
            nice = False
            break
        i += 1
    if line[i] in 'aeiou': vow += 1
            
    if nice and vow >= 3 and dub: nice_str[0] = 1

    # Part 2
    i, pairs, pair, skip, dub = 0, set(), False, False, False
                
    while i < end - 1:
        if line[i] == line[i+2]: dub = True
        p = line[i:i+2]
        if not skip:
            if p not in pairs: pairs.add(p)
            else:              pair = True
        else: skip = False
                    
        if line[i] == line[i+1] and line[i] == line[i+2]: skip = True
        i += 1
    if line[i:] in pairs: pair = True

    if pair and dub: nice_str[1] = 1
   
    return nice_str

def main():
    with open('d05') as f:
        lines = f.readlines()
        strings = list(map(nice_strings, lines))
        print('P1:', sum(p[0] for p in strings))
        print('P2:', sum(p[1] for p in strings))

if __name__ == "__main__":
    main()
