'''
AoC 2016 Day 20 parts 1 & 2
'''

from sys import argv

ip_ranges = []

def get_ips():
    global ip_ranges

    with open(argv[1]) as f: rl = f.readlines()
    rl = [l.strip().split('-') for l in rl]
    ip_ranges = sorted([[int(l[0]), int(l[1])] for l in rl], key=lambda x: x[0])

def check_ips():
    global ip_ranges

    i, total = 0, 0
    while i < len(ip_ranges) - 1:
        r0, r1 = ip_ranges[i], ip_ranges[i+1]
        if r0[1] >= r1[0] - 1:
            r1[0] = r0[0]
            if r0[1] > r1[1]: r1[1] = r0[1] 
            ip_ranges.remove(r0)
        else:
            total += r1[0] - r0[1] - 1
            i += 1

    total += 2 ** 32 - ip_ranges[i][1] - 1
    
    return ip_ranges[0][1] + 1, total


def main():
    get_ips()
    lo, total = check_ips()
    print('Lowest:', lo, '\nValid:', total)

if __name__ == '__main__':
    main()
