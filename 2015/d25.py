'''
AoC 2015 Day 25 Parts 1 & 2
'''

d, r, c, curr = 20151125, 1, 1, 1

while True:
    d = (d * 252533) % 33554393

    if r == 1:
        curr += 1
        r, c = curr, 1
    else:
        r -= 1
        c += 1

    if r == 2978 and c == 3083: break

print(d)
