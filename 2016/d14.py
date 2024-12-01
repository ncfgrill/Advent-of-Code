'''
AoC 2016 Day 14 parts 1 & 2
'''

from hashlib import md5

fives, index = {}, 0

def get_hash(salt, num, p):
    i, value = 0, md5((salt + str(num)).encode()).hexdigest()

    if p == 2:
        while i < 2016:
            value = md5(value.encode()).hexdigest()
            i += 1

    return value

def check_three(value):
    i = 0

    while i < len(value) - 2:
        if value[i:i+3] == value[i] * 3: return value[i]
        i += 1

def check_five(salt, num, check, p):
    global index

    i = max(num, index)
    while i < num + 1000:
        value, j = get_hash(salt, i, p), 0

        while j < len(value) - 4:
            save = value[j]
            if value[j:j+5] == save * 5:
                if save not in fives: fives[save] = {i}
                else: fives[save].add(i)
                
                if save == check:
                    index = i
                    return True
                j += 4
            j += 1
        i += 1
    index = i
    return False

def find_key(p):
    global fives

    salt, num, total_keys = 'qzyelonm', -1, 0
    
    while total_keys < 64:
        num += 1
        value = get_hash(salt, num, p)

        trip = check_three(value)
        if trip in fives:
            for f in list(fives[trip]):
                if f > num and f <= num + 1000:
                    total_keys += 1
                    break
        elif check_five(salt, num + 1, trip, p):
            total_keys += 1
    return num

def main():
    global fives, index

    print('Index:', find_key(1))
    fives, index = {}, 0
    print('Index:', find_key(2))

if __name__ == "__main__":
    main()
