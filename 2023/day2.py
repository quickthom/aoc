
from cmn import loadfile
import math


sample = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


class Game:
    def __init__(self, id):
        self.id = id
        self.cubes = dict()
        self.reveals = []

    def initialize(self, gamestr):
        reveals = gamestr.split('; ')
        for reveal in reveals:
            rev = dict()
            for revstr in reveal.split(', '):
                n, color = revstr.split(' ')
                rev[color] = int(n)
            self.reveals.append(rev)
    
    def possible(self, limits):
        for reveal in self.reveals:
            for color, n in reveal.items():
                if n > limits[color]:
                    return False
        return True
    
    def min_set(self):
        res = dict()
        for color in ['red','blue','green']:
            counts = [rev[color] for rev in self.reveals if color in rev]
            res[color] = max(counts)
        return res
    
    def game_power(self):
        return math.prod(self.min_set().values())
    def __repr__(self):
        return f"Game {self.id}"

data = sample.split("\n")[1:-1]
data = loadfile('day2.txt', 'https://adventofcode.com/2023/day/2/input')

games = []
for s in data:
    n = int(s.split(':')[0].split()[1])
    g = Game(n)
    g.initialize(s.split(':')[1].strip())
    games.append(g)


limits = dict(green=13, blue=14, red=12)
print(sum([g.possible(limits) * g.id for g in games]))
print(sum([g.game_power() for g in games]))

