from handy import read
import numpy as np

breaker = ' -> '

lines = read(5)
"""lines = ["0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2"]"""
pairs= list(map(lambda x: (tuple(map(int, x[0].split(','))), 
                      tuple(map(int, x[1].split(',')))
                      ), 
        [x.split(breaker) for x in lines]))

max_dim = max(list(map(lambda x: max([max(x[0]), max(x[1])]), pairs))) + 1

grid = np.zeros(max_dim**2).reshape((max_dim, max_dim))

for (x1, y1), (x2, y2) in pairs:
    if x1 == x2:
        ylow, yhi = min(y1,y2), max(y1,y2)
        for y in range(ylow, yhi+1):
            grid[x1, y] += 1
    elif y1 == y2:
        xlow, xhi = min(x1,x2), max(x1,x2)
        for x in range(xlow, xhi+1):
            grid[x, y1] += 1
    else:
        xslope = 1 - 2 * (x2 < x1)
        yslope = 1 - 2 * (y2 < y1)

        y = y1
        for x in range(x1, x2+xslope, xslope):
            grid[x, y] += 1
            y += yslope
print('At least one line:', (grid > 0).sum())
print('At least two lines:', (grid > 1).sum())
print('At least three lines:', (grid > 2).sum())

        

