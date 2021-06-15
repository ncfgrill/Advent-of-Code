'''
AoC 2015 Day 21 Parts 1 & 2
'''

from math import ceil

weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
armor = [(13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
rings = [(25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]
b_hp, b_damage, b_armor = 0, 0, 0

def battle(p_damage, p_armor):
    global b_hp, b_damage, b_armor

    p_d = max(1, p_damage - b_armor)
    b_d = max(1, b_damage - p_armor)

    return ceil(100 / b_d) >= ceil(b_hp / p_d)

def create_boss():
    global b_hp, b_damage, b_armor

    with open('d21') as f:
        stats, lines = [], f.readlines()
        for l in lines:
            l = l.split(':')
            stats.append(int(l[1].strip()))
    b_hp, b_damage, b_armor = stats[0], stats[1], stats[2]

def play():
    create_boss()
    min_cost, max_cost = 999, 0
    
    for w in weapons:
        for a in armor:
            if battle(w[1], a[2]):
                min_cost = min(min_cost, w[0] + a[0])
            else:
                max_cost = max(max_cost, w[0] + a[0])
            
            for i in range(0, len(rings)):
                for j in range(i, len(rings)):
                    c = min(j - i, 1)
                    if battle(w[1] + rings[i][1] + c * rings[j][1],
                              a[2] + rings[i][2] + c * rings[j][2]):
                        min_cost =\
                            min(min_cost,
                                w[0] + a[0] + rings[i][0] + c * rings[j][0])
                    else:
                        max_cost =\
                            max(max_cost,
                                w[0] + a[0] + rings[i][0] + c * rings[j][0])

    return min_cost, max_cost

def main():
    win, lose = play()
    print('Minimum cost win:', win)
    print('Maximum cost lose:', lose)

if __name__ == "__main__":
    main()
