'''
AoC 2015 Day 16 Parts 1 & 2
'''

sues, wrong1, wrong2 = [], [], []
ticker = {'children' : 3,
          'cats' : 7,
          'samoyeds' : 2,
          'pomeranians' : 3,
          'akitas' : 0,
          'vizslas' : 0,
          'goldfish' : 5,
          'trees' : 3,
          'cars' : 2,
          'perfumes' : 1}

class AuntSue:
    def __init__(self, name):
        self.name = name
        self.items = {}

def get_sues():
    with open('d16') as f:
        for l in f.readlines():
            l = l.strip().split(' ')
            s = AuntSue(l[1].strip(':'))
            l, i = l[2:], 0

            while i < len(l):
                s.items[l[i].strip(':')] = int(l[i+1].strip(','))
                i += 2

            sues.append(s)

def check_sues():
    get_sues()
    ranges = ['cats', 'trees', 'pomeranians', 'goldfish']
    for s in sues:
        for i in s.items:
            if i == ranges[0] or i == ranges[1]:
                if s.items[i] <= ticker[i]:
                    wrong2.append(int(s.name))
            if i == ranges[2] or i == ranges[3]:
                if s.items[i] >= ticker[i]:
                    wrong2.append(int(s.name))
            if s.items[i] != ticker[i]:
                wrong1.append(int(s.name))
                if i not in ranges: wrong2.append(int(s.name))

def main():
    check_sues()
    all_nums = {i for i in range(1, 501)}
    s1, s2 = (all_nums - set(wrong1)).pop(), (all_nums - set(wrong2)).pop()
    print('Sue:', s1, '\nReal Sue:', s2)

if __name__ == "__main__":
    main()
