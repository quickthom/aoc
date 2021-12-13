from handy import read
from collections import defaultdict as dd

data = read(12)

def can(c, sv):
    if c == 'start':
        return False
    elif c.isupper():
        return True
    elif len(sv) == 0 or max(sv.values()) > 1:
        return sv[c] < 1
    else:
        return sv[c] < 2

def go(c, sv):
    if c.islower():
        sv[c] += 1
    routes = 0
    for dest in edg[c]:
        if dest == 'end':
            routes += 1
        elif can(dest, sv):
            routes += go(dest,sv.copy())
    return routes

edg = dd(set)

for c1, c2 in [x.split('-') for x in data]:
    edg[c1].add(c2)
    edg[c2].add(c1)

print(go('start', dd(int)))
