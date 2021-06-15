'''
AoC 2015 Day 11 Parts 1 & 2
'''

password, inc, d1, d2 = 'cqjxjnds', False, False, False
counter, i = [ord(i) - ord('a') for i in password], len(password) - 1
bad = [ord('i'), ord('l'), ord('o')]

def check_bad_letters():
    global i

    for j in range(i + 1):
        if counter[j] in bad:
            counter[j] += 1
            j += 1
            while j < i + 1: counter[j] = 0
            return True
    return False

def check_inc():
    global i, inc

    for j in range(i - 1):
        if counter[j+1] == counter[j] + 1 and counter[j+2] == counter[j] + 2:
            inc = True
            return True
    return False

def check_dubs():
    global i, d1, d2

    j, d1, d2 = 0, False, False
    while j < i:
        if counter[j] == counter[j+1]:
            if d1: d2 = True
            else:
                d1 = True
                j += 1
        if d1 and d2: return True
        j += 1
    return False

def convert():
    new = ''
    for j in counter: new += chr(j + ord('a'))
    return new

def increment():
    global i, inc, d1, d2, counter, password

    while not (inc and d1 and d2):
        counter[i] += 1
        if counter[i] == 26:
            counter[i], j = 0, i - 1
            while True:
                counter[j] += 1
                if counter[j] == 26:
                    counter[j] = 0
                    j -= 1
                else: break

        if not check_bad_letters():
            if check_inc():
                if check_dubs():
                    password = convert()
                    return password

def main():
    global counter, inc, d1, d2

    print('New password:', increment())
    counter = [ord(i) - ord('a') for i in password]
    inc, d1, d2 = False, False, False
    print('New new password:', increment())

if __name__ == "__main__":
    main()
