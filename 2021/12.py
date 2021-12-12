from handy import read, read_test, E
from collections import defaultdict

lines = read(12)
#lines = read_test(12)

caves = dict()
small = set('abcdefghijklmnopqrstuvwxyz')

class Cave:
    def __init__(self, name):
        self.name = name
        self.links = set()
        if len(set(self.name) - small) == 0:
            self.size = 'small'
        else:
            self.size = 'large'
    def link_to(self, cave):
        self.links.add(cave)

for line in lines:
    c1, c2 = line.split('-')
    if c1 not in caves:
        caves[c1] = Cave(c1)
    if c2 not in caves:
        caves[c2] = Cave(c2)
    caves[c1].link_to(caves[c2])
    caves[c2].link_to(caves[c1])

def can_go(cave, visited):
    if cave.name =='start':
        return False
    if cave.size == 'large':
        return True
    if len(visited) == 0 or max(visited.values()) > 1:
        smallcap = 1
    else:
        smallcap = 2
    if visited[cave] < smallcap:
        return True
    return False

def reach_end_from(cave, visited):
    routes = 0
    for dest in cave.links:
        if dest.name == 'end':
            routes += 1
        elif not can_go(dest, visited):
            continue
        else:
            v = visited.copy()
            if dest.size == 'small':
                v[dest] += 1
            routes += reach_end_from(dest,v )
    return routes


visited = defaultdict(int)
print(reach_end_from(caves['start'], visited))
