from handy import *
from collections import deque

lines = read(24)
#lines = read_test(24)

blacks = set()
all_tiles =set()
for line in lines:
    loc = [0,0]
    q = deque(line)

    while q:
        d = q.popleft()
        if d in 'ns':
            if d == 'n':
                loc[0] += 1
            else:
                loc[0] -= 1
            d = q.popleft()
            if d == 'e':
                loc[1] += 0.5
            elif d == 'w':
                loc[1] -= 0.5
        else:
            if d == 'e':
                loc[1] += 1
            elif d == 'w':
                loc[1] -= 1
        all_tiles.add(tuple(loc))

    if tuple(loc) in blacks:
        blacks.remove(tuple(loc))
    else:
        blacks.add(tuple(loc))

print(len(blacks))

def get_neighbors(r,c):
    return {(r,c+1),(r,c-1),(r+1,c+0.5),(r+1,c-0.5),(r-1,c+0.5),(r-1,c-0.5)}

for day in range(100):
    r_range = (min([r for r,c in all_tiles])-2-day, max([r for r,c in all_tiles])+2+day)
    c_range = (int(2*min([c for r,c in all_tiles]))-2-day, int(2*max([c for r,c in all_tiles]))+2+day)
    flips = set()
    for r in range(*r_range):
        for c in range(*c_range):
            c /= 2
            adj_black = len(blacks & get_neighbors(r,c))
            if (r,c) in blacks:
                if adj_black == 0 or adj_black > 2:
                    flips.add((r,c))
            elif adj_black == 2:
                flips.add((r,c))
    blacks ^= flips 
    print("Day",day+1,len(blacks))

