'''
AoC 2016 Day 5 parts 1 & 2
'''

from hashlib import md5

def main():
    key, num = 'ffykfhsq', 0
    pass_easy, pass_hard = '', ['-','-','-','-','-','-','-','-']

    print('Password:', ''.join(p for p in pass_hard))
    while '-' in pass_hard:
        num += 1
        value = md5((key + str(num)).encode()).hexdigest()

        if value[:5] == '00000':
            v = value[5]
            if len(pass_easy) < 8: pass_easy += v
            try:
                v = int(v)
                if v < 8 and pass_hard[v] == '-':
                    pass_hard[v] = value[6]
                    print('Password:', ''.join(p for p in pass_hard))
            except ValueError: continue

    print('Easy:', pass_easy, '\nHard:', ''.join(p for p in pass_hard))

if __name__ == "__main__":
    main()
