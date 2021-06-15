'''
AoC 2015 Day 8 Parts 1 & 2
'''

def get_characters():
    v1, v2 = 0, 0

    with open('d08') as f:
        for l in f:
            l, i = l.strip('\n'), 1
            s_l = len(l)
            s1, s2 = s_l - 2, s_l + 4
            
            while i < s_l - 1:
                if l[i] == '\\':
                    if l[i+1] == '\\' or l[i+1] == '\"':
                        s1 -= 1
                        s2 += 2
                        i += 1
                    elif l[i+1] == 'x':
                        s1 -= 3
                        s2 += 1
                        i += 3

                i += 1

            v1 += s_l - s1
            v2 += s2 - s_l
        return v1, v2

def main():
    v1, v2 = get_characters()
    print('String literal - chars in mem:', v1)
    print('Newly encoded - string literal:', v2)

if __name__ == "__main__":
    main()
