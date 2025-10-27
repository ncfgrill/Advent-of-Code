'''
AoC 2015 Day 4 parts 1 & 2
'''

from hashlib import md5
from sys import argv

def main():
    key, value, num, five_found = argv[1], '', 0, False

    while value[:6] != '0'*6:
        num += 1
        value = md5((key + str(num)).encode()).hexdigest()

        if value[:5] == '00000' and not five_found:
            print('Five zero hash:', num)
            five_found = True

    print('Six zero hash:', num)

if __name__ == "__main__":
    main()
