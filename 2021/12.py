from handy import read
from collections import defaultdict

lines = read(12)

caves = dict()

class Cave:
    def __init__(self, name):
        self.name = name
        self.links = set()
        self.size = 'small' if self.name.islower() else 'large'
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
    elif cave.size == 'large':
        return True
    elif len(visited) == 0 or max(visited.values()) > 1:
        return visited[cave] < 1
    else:
        return visited[cave] < 2
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
            routes += reach_end_from(dest,v)
    return routes


visited = defaultdict(int)
print(reach_end_from(caves['start'], visited))
