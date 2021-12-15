from handy import read_grid
import numpy as np

grid = read_grid(15,col_delim="")

g = np.array(grid.lines)
for i in range(4):
    grid.apply(lambda x: x+1 if x < 9 else 1)
    g = np.concatenate([g, np.array(grid.lines)])
g_sing = g.copy()
for i in range(4):
    g = np.concatenate([g, g_sing+i+1], 1)
g[g>9] = g[g>9]-9

grid.lines = g
grid.height, grid.width = g.shape

start = (0,0)
scores = np.ones_like(g)*100000

scores[0,0] = 0
scores[0,1] = grid[0,1]
scores[1,0] = grid[1,0]

def run(grid, scores):
    for r in range(grid.height):
        for c in range(grid.width):
            if (r,c) == start:
                continue
            surroundings = [scores[x,y] for x,y in grid.get_4_neighbors(r,c)]
            scores[r,c] = min([scores[r,c]]+surroundings)+grid[r,c]

oldsum = sum(scores).sum()
oldmin = scores[grid.height-1,grid.width-1]

tolerance = 10
for i in range(500):
    run(grid,scores)
    newsum = sum(scores).sum()
    newmin = scores[grid.height-1,grid.width-1]
    print(newsum,scores[grid.height-1, grid.width-1])
    if newmin == oldmin:
        tolerance -= 1
    else:
        tolerance = 10
    if oldsum==newsum or tolerance <= 0:
        print('Converge')
        break
    oldsum = newsum
    oldmin=newmin
        
