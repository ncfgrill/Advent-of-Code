'''
AoC 2015 Day 19 Parts 1 & 2
'''

from sys import argv

molecules, orig = {}, ''

def get_molecules():
    global molecules, orig

    with open(argv[1]) as f:
        for l in f.readlines():
            l = l.strip().split(' => ')
            if len(l) > 1:
                if l[0] in molecules: molecules[l[0]].append(l[1])
                else: molecules[l[0]] = [l[1]]
            elif len(l) == 1: orig = l[0].strip()

def replace():
    global molecules, orig

    created = set()
    for m in molecules:
        l = len(m)
        for r in molecules[m]:
            i = 0
            while i < len(orig) - l + 1:
                if orig[i:i+l] == m:
                    created.add(orig[:i] + r + orig[i+l:])
                    i += l
                else: i += 1

    return len(created)

def molecule_reverse():
    global molecules

    rev = {}
    for m in molecules:
        for r in molecules[m]: rev[r] = m

    return rev

def construct():
    global molecules, orig

    rev, save, count = molecule_reverse(), orig, 0
    while save != 'e':
        for m in rev:
            if m in save:
                i, l = save.index(m), len(m)
                save = save[:i] + rev[m] + save[i+l:]
                count += 1

    return count

def main():
    get_molecules()
    print('Distinct molecules:', replace())
    print('Construction steps:', construct())

if __name__ == "__main__":
    main()
