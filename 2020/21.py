from handy import *
from collections import defaultdict,Counter

lines = read(21)
#lines = read_test(21)

foods = []
pos = defaultdict(set)
allings=set()
pos2 = dict()
for line in lines:
    t1, t2 = line[:-1].split(' (')
    ingreds, allergens = (set(t1.split()), set(t2[9:].split(', ')))
    foods.append((ingreds,allergens))

    allings |= ingreds
    for a in allergens:
        if a not in pos2:
            pos2[a] = ingreds.copy()
        else:
            pos2[a] &= ingreds
        
    for i in ingreds:
        for a in allergens:
            pos[i].add(a)

nonalg = allings - set.union(*pos2.values())
ctr = Counter(' '.join(lines).split())
print(sum([ctr[x] for x in nonalg]))
h = 1000
def go(pos2):
    global h
    while sum([len(x) for x in pos2.values()]) < h:
        h = sum([len(x) for x in pos2.values()])

        for a,ings in pos2.copy().items():
            if len(ings) == 1:
                for a2, ings2 in pos2.copy().items():
                    if a==a2: continue
                    pos2[a2] = ings2 - ings
    return pos2
out = go(pos2)
sortout = ','.join([out[x].pop() for x in sorted(out.keys())])
print(sortout)

