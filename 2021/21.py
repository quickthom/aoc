from handy import *
from collections import Counter

lines = read(21)
#lines = read_test(21)

p1 = int(lines[0].split()[-1])
p2 = int(lines[1].split()[-1])

p1s = 0
p2s = 0
rolls = 0
def roll():
    global rolls
    i = 1
    while True:
        if i > 100:
            i = 1
        rolls += 1
        yield i
        i += 1

def incr(space, n):
    move = n % 10
    for i in range(move):
        if space == 10:
            space = 1
        else:
            space += 1
    return space

incrs = dict()
for space in range(1,11):
    for roll in range(3,10):
        incrs[(space,roll)] = incr(space, roll)

from itertools import product
die_options = product((1,2,3),(1,2,3),(1,2,3))
die_option_sums = [sum(x) for x in die_options]
die_options_2p = list(product(die_option_sums, die_option_sums))
die_opt_counts = Counter(die_options_2p)

def play_turn(p1,p2,p1s,p2s,xz):
    p1w, p2w = 0, 0
    for (roll1, roll2), ct in die_opt_counts.items():
        if xz: print(roll1,roll2,p1w,p2w)
        new_p1 = incrs[p1, roll1]
        new_p1s = p1s+new_p1
#        print('P1:',p1,'Roll:',roll1,'New pos:',new_p1,'New score:',new_p1s)
        if new_p1s >= 21:
            p1w += ct
            continue
        new_p2 = incrs[p2, roll2]
        new_p2s = p2s+new_p2
#        print('P2:',p2,'Roll:',roll2,'New pos:',new_p2,'New score:',new_p2s)
        if new_p2s >= 21:
            p2w += ct
            continue
        a, b = play_turn(new_p1, new_p2, new_p1s, new_p2s,False)
        p1w += a*ct
        p2w += b*ct
    return p1w, p2w

w1, w2 = play_turn(p1,p2,p1s,p2s,True)
print(int(w1/27), w2)

#winner = play_game()
#if winner == 1:
#    loser_score = p2s
#else:
#    loser_score = p1s

#print(loser_score*rolls)

