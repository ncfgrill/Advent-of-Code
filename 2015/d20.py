'''
AoC 2015 Day 20 Parts 1 & 2
'''

from math import ceil, sqrt

def check_prime(num):
    if num <= 3:                        return num > 1
    elif num % 6 != 1 and num % 6 != 5: return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0: return False

    return True

def sum_factors(num, mode):
    factors = set()

    for i in range(1, ceil(sqrt(num)) + 1):
        if num % i == 0:
            if mode == 0: factors.update([i, num // i])
            else:
                if (num // i) * 50 >= num: factors.add(num // i)
                if i * 50 >= num: factors.add(i)

    return sum(factors) * 10 if mode == 0 else sum(factors) * 11

def find_house(mode):
    h, total, presents = 0, 0, 29000000

    while total <= presents:
        h += 1
        #if check_prime(h): continue
        total = sum_factors(h, mode)

    return h

def main():
    print('House:', find_house(0))
    print('House:', find_house(1))

if __name__ == "__main__":
    main()
