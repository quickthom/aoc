import time
from cmn import loadfile, preproc
import math
data = loadfile('day4.txt', 'https://adventofcode.com/2023/day/4/input')

sample = '''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
# data = preproc(sample)

class Card:
    def __init__(self, s):
        self.s = s
        head, foot = s.split(': ')
        self.id = int(head.split(' ')[-1])
        self._match_count = None
        self.win, self.sel = [x.split() for x in foot.strip().split(' | ')]

    def get_matches(self):
        return set(self.win).intersection(self.sel)
    
    def match_count(self):
        if self._match_count is None:
            self._match_count = len(self.get_matches())
        return self._match_count
    
    def adders(self):
        return [self.id+i+1 for i in range(self.match_count())]
    
    def score(self):
        matches = self.get_matches()
        if len(matches) <= 0:
            return 0
        else:
            return 2**(len(matches)-1)
    
    def copy(self):
        return Card(self.s)
    def __repr__(self):
        return "Card "+str(self.id)

def get_card(n):
    ret = [c for c in all_cards if c.id==n]
    if len(ret) < 1:
        return None
    else:
        return ret[0]

all_cards = [Card(x) for x in data]
cards = [Card(x) for x in data]
card_wins = {}
while len(card_wins) < len(all_cards):
    for c in cards:
        if c in card_wins:
            continue
        ready = True
        adders = c.adders()
        tot = 1
        for a in adders:
            if a in card_wins:
                tot += card_wins[a]
            else:
                ready = False
        if ready:
            card_wins[c.id] = tot
    print(len(card_wins), end=".")
print("\n",sum(card_wins.values()))
            


max_card = max([c.id for c in cards])
assert all([len(c.sel)==len(set(c.sel)) for c in cards])
assert all([len(c.win)==len(set(c.win)) for c in cards])
print(sum([c.score() for c in cards]))

i = 0
start = time.time()
total_card_count = 0
while len(cards) > 0:
    c = cards.pop()
    total_card_count += 1
    for j in range(c.match_count()):
        if c.id+j+1 <= max_card:
            cards.append(get_card(c.id+j+1))
    i += 1
    if i % 500000 == 0: print(len(cards), end=" . ")
    
print(i)

