'''
AoC 2015 Day 22 Parts 1 & 2
'''

min_mana = 999999999

class Boss:
    def __init__(self, hp, damage):
        self.hp, self.damage = hp, damage

class Wizard:
    def __init__(self, hp, mana, armor, effects, used):
        self.hp, self.mana = hp, mana
        self.armor, self.effects, self.used = armor, effects, used
        self.spells = [self.magic_missile,
                       self.drain,
                       self.shield,
                       self.poison,
                       self.recharge]

    def magic_missile(self, other): # 0
        self.mana -= 53
        self.used += 53
        other.hp -= 4

    def drain(self, other): # 1
        self.mana -= 73
        self.used += 73
        self.hp += 2
        other.hp -= 2

    def shield(self, other): # 2
        self.mana -= 113
        self.used += 113
        self.effects[2] = 6

    def poison(self, other): # 3
        self.mana -= 173
        self.used += 173
        self.effects[3] = 6

    def recharge(self, other): # 4
        self.mana -= 229
        self.used += 229
        self.effects[4] = 5

    def check_effects(self, other):
        for e in list(self.effects.keys()):
            if e == 2: self.armor = 7
            elif e == 3: other.hp -= 3
            else: self.mana += 101
            
            if self.effects[e] == 1: del self.effects[e]
            else: self.effects[e] -= 1

def create_boss():
    with open('d22') as f:
        stats, lines = [], f.readlines()
        for l in lines:
            l = l.split(':')
            stats.append(int(l[1].strip()))

    return Boss(stats[0], stats[1])

def battle(w, b, d):
    global min_mana

    for i in range(len(w.spells)):
        # Create copies
        new_w = Wizard(w.hp, w.mana, w.armor, w.effects.copy(), w.used)
        new_b = Boss(b.hp, b.damage)
    
        # WIZARD TURN
        if d == 1: new_w.hp -= 1 # Hard mode

        # Check current effects
        new_w.check_effects(new_b)
        if new_b.hp <= 0:
            min_mana = min(min_mana, new_w.used)
            continue
        
        # Check if spell is currently in effect (can't cast, move on)
        if i in new_w.effects: continue

        # Cast new spell
        new_w.spells[i](new_b)
        if new_w.mana < 0 or new_w.used >= min_mana: continue
        new_w.armor = 0

        # BOSS TURN
        # Check current effects
        new_w.check_effects(new_b)
        if new_b.hp <= 0:
            min_mana = min(min_mana, new_w.used)
            continue

        # Boss attacks
        new_w.hp -= max(1, new_b.damage - new_w.armor)
        if d == 1 and new_w.hp == 1: continue
        if new_w.hp > 0: battle(new_w, new_b, d)

def main():
    global min_mana

    w, b = Wizard(50, 500, 0, {}, 0), create_boss()

    battle(w, b, 0)
    print('Min mana easy:', min_mana)

    w, b, min_mana = Wizard(50, 500, 0, {}, 0), create_boss(), 999999
    battle(w, b, 1)
    print('Min mana hard:', min_mana)
if __name__ == "__main__":
    main()
