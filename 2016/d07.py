'''
AoC 2016 Day 7 Parts 1 & 2
'''

def get_ips():
    with open('d07') as f: lines = f.readlines()
    return [l.strip() for l in lines]

def check_tls(ip):
    in_b, abba, i = 0, False, 0
    while i < len(ip) - 3:
        if ip[i] == '[': in_b += 1
        elif ip[i] == ']': in_b -= 1
        else:
            if ip[i] != ip[i+1] and ip[i:i+2] == ip[i+3:i+1:-1]:
                if in_b != 0: return 0
                abba = True
        i += 1
    return 1 if abba else 0

def check_ssl(ip):
    in_b, aba, aba_b, i = 0, set(), set(), 0
    while i < len(ip) - 2:
        if ip[i] == '[': in_b += 1
        elif ip[i] == ']': in_b -= 1
        elif ip[i] == ip[i+2] and ip[i+1] not in '[]':
            check = ip[i:i+2]
            if in_b == 0:
                if check[::-1] in aba_b: return 1
                aba.add(check)
            else:
                if check[::-1] in aba: return 1
                aba_b.add(check)
        i += 1    
    return 0

def main():
    ip = get_ips()
    print('TLS:', sum(map(check_tls, ip)))
    print('SSL:', sum(map(check_ssl, ip)))

if __name__ == "__main__":
    main()
