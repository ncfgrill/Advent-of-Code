'''
AoC 2015 Day 15 Parts 1 & 2
'''

ingredients = []

class Ingredient:
    def __init__(self, cap, dur, fla, tex, cal):
        self.cap, self.dur, self.fla = cap, dur, fla
        self.tex, self.cal = tex, cal

def get_ingredients():
    with open('d15') as f:
        for l in f.readlines():
            l = l.strip().split(' ')
            ingredients.append(Ingredient(int(l[2].strip(',')),
                                          int(l[4].strip(',')),
                                          int(l[6].strip(',')),
                                          int(l[8].strip(',')),
                                          int(l[10])))

def find_combo():
    get_ingredients()
    score, score_cal, amts = 0, 0, [0, 0, 0, 0]

    while amts[2] < 98:
        amts[3] = 100 - amts[0] - amts[1] - amts[2]
        if amts[3] >= 0:
            cap, dur, fla, tex, cal = 0, 0, 0, 0, 0
            for i, ing in enumerate(ingredients):
                amt = amts[i]
                cap += amt * ing.cap
                dur += amt * ing.dur
                fla += amt * ing.fla
                tex += amt * ing.tex
                cal += amt * ing.cal

            if cap > 0 and dur > 0 and fla > 0 and tex > 0:
                s = cap * dur * fla * tex
                if s > score: score = s
                if s > score_cal and cal == 500: score_cal = s

        if amts[0] > 97 or amts[3] < 0:
            amts[0] = 1
            amts[1] += 1

        if amts[1] > 97:
            amts[1] = 1
            amts[2] += 1
        
        amts[0] += 1

    return score, score_cal

def main():
    s, s_c = find_combo()
    print('No cal limit:', s, '\n500 cal limit:', s_c)

if __name__ == "__main__":
    main()
