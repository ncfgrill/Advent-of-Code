'''
AoC 2017 Day 1 Parts 1 & 2
'''

def main():
    with open('d01') as f: seq = f.readline().strip()

    seq_sum_1, seq_sum_2, seq_len = 0, 0, len(seq)
    for i in range(seq_len):
        if seq[i] == seq[(i + 1) % seq_len]:
            seq_sum_1 += int(seq[i])
        if seq[i] == seq[(i + (seq_len // 2)) % seq_len]:
            seq_sum_2 += int(seq[i])

    print('Part 1: {}'.format(seq_sum_1))
    print('Part 2: {}'.format(seq_sum_2))

if __name__ == '__main__':
    main()
