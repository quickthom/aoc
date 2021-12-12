from handy import read
from collections import defaultdict

lines = read(12)

def can_go(cave, small_visits):
    if cave == 'start':
        return False
    elif cave.isupper():
        return True
    elif len(small_visits) == 0 or max(small_visits.values()) > 1:
        return small_visits[cave] < 1
    else:
        return small_visits[cave] < 2

def reach_end_from(cave, small_visits):
    if cave.islower():
        small_visits[cave] += 1
    routes = 0
    for dest in links[cave]:
        if dest == 'end':
            routes += 1
        elif can_go(dest, small_visits):
            routes += reach_end_from(dest,small_visits.copy())
    return routes

small_visits = defaultdict(int)
links = defaultdict(set)

for c1, c2 in [x.split('-') for x in lines]:
    links[c1].add(c2)
    links[c2].add(c1)

print(reach_end_from('start', small_visits))
