'''
AoC 2016 Day 15 parts 1 & 2
'''

discs = []

class Disc:
    def __init__(self, pos, curr):
        self.pos, self.curr = pos, curr

def get_discs():
    global discs

    with open('d15') as f: lines = f.readlines()
    lines = [l.strip().split(' ') for l in lines]
    for l in lines: discs.append(Disc(int(l[3]), int(l[-1][0])))

def press_button():
    global discs

    t, drop = -1, False
    while not drop:
        t += 1
        drop = True
        for i, d in enumerate(discs):
            if (d.curr + t + i + 1) % d.pos != 0:
                drop = False
                break
    return t

def main():
    global discs

    get_discs()
    print('Time:', press_button())
    discs.append(Disc(11, 0))
    print('Time:', press_button())

if __name__ == "__main__":
    main()
