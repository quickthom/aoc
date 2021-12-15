from handy import *

grid = read_test_grid(11,col_delim="",dtype=str)
#grid = read_grid(11,col_delim="",dtype=str)

def update(grid, fill, empty):
    for f in fill:
        grid[f] = '#'
    for e in empty:
        grid[e] = 'L'

def friend_count(grid, p):
    return sum([1 for r,c in grid.get_8_neighbors(*p) if grid[r,c] == '#'])

def visible_friend_count(grid, p):
    pr, pc = p
    ns = grid.get_8_neighbors(*p)
    for r,c in ns.copy():
        if grid[r,c] == '.':
            ns.remove((r,c))
            newr, newc = r, c
            while True:
                newr, newc = newr + (r-pr), newc + (c-pc)
                if newr >= 0 and newc >= 0 and newr < grid.height and newc < grid.width:
                    if grid[newr,newc] != '.':
                        ns.append((newr, newc))
                        break
                else:
                    break
    return sum([1 for r,c in ns if grid[r,c] == '#'])



def iterate(grid):
    pts = grid.scan()
    fill, empty = [],[]
    for r,c in pts:
        if grid[r,c] == '.':
            continue
        elif grid[r,c] == '#':
            if friend_count(grid, (r,c)) >= 4:
                empty.append((r,c))
        elif grid[r,c] == 'L':
            if friend_count(grid, (r,c)) == 0:
                fill.append((r,c))
    update(grid, fill, empty)

def occupied_seats(grid):
    return sum((grid[r,c]=='#' for r,c in grid.scan()))

occ = -1
while occ != occupied_seats(grid):
    occ = occupied_seats(grid)
    iterate(grid)

print(occ)
def iterate2(grid):
    pts = grid.scan()
    fill, empty = [],[]
    for r,c in pts:
        if grid[r,c] == '.':
            continue
        elif grid[r,c] == '#':
            if visible_friend_count(grid, (r,c)) >= 5:
                empty.append((r,c))
        elif grid[r,c] == 'L':
            if visible_friend_count(grid, (r,c)) == 0:
                fill.append((r,c))
    update(grid, fill, empty)

grid = read_grid(11,col_delim="",dtype=str)
occ = -1
while occ != occupied_seats(grid):
    occ = occupied_seats(grid)
    iterate2(grid)
print(occ)
