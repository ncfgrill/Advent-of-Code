'''
AoC 2015 Day 14 Parts 1 & 2
'''

reindeer, distance, points = [], [], []

class Reindeer:
    def __init__(self, speed, duration, rest):
        self.speed = speed
        self.duration = duration
        self.rest = rest
        self.is_resting = rest
        self.is_moving = duration

def create_reindeer():
    with open('d14') as f:
        for l in f.readlines():
            l = l.strip().split(' ')
            reindeer.append(Reindeer(int(l[3]), int(l[6]), int(l[13])))
            distance.append(0)
            points.append(0)

def calculate():
    create_reindeer()
    time = 0
    while time < 2503:
        for i, r in enumerate(reindeer):
            if not r.is_resting and not r.is_moving:
                r.is_resting, r.is_moving = r.rest, r.duration
            if r.is_moving:
                distance[i] += r.speed
                r.is_moving -= 1
            else: r.is_resting -= 1

        max_d, r = 0, []
        for i, d in enumerate(distance):
            if d >= max_d:
                if d > max_d:
                    r.clear()
                    max_d = d
                r.append(i)

        for i in r: points[i] += 1
        
        time += 1

    return max(distance), max(points)

def main():
    d, p = calculate()
    print('Distance:', d, '\nPoints:', p)

if __name__ == "__main__":
    main()
