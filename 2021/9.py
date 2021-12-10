from handy import read
import numpy as np

lines = read(9)
"""lines = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
        ]
"""
lnlen = len(lines[0])
lines = ["9"*lnlen]+lines+["9"*lnlen]
lines = ["9"+x+"9" for x in lines]

lines = [list(map(int, x)) for x in lines]
data = np.array(lines)

out =[]
low_points = []
for row in range(1, len(lines)-1):
    for col in range(1, lnlen+1):
        left = data[row,col] < data[row,col-1]
        right = data[row,col] < data[row,col+1]
        up = data[row,col] < data[row-1,col]
        down = data[row,col] < data[row+1,col]
        if left and right and up and down:
            out.append(data[row,col]+1)
            low_points.append((row,col))

print("Part One:",sum(out))

def get_basin_neighbors(r, c):
    out = set()
    for rr, cc in ((r-1, c),(r+1,c),(r,c-1),(r,c+1)):
      if data[rr, cc] < 9:
          out.add((rr,cc))
    return out

def get_basin(low_point):
    out = set()
    neighbors = get_basin_neighbors(*low_point)
    while len(neighbors - out) > 0:
      for n in (neighbors - out):
          out.add(n)
          neighbors |= get_basin_neighbors(*n)
    return out

basins = {p: get_basin(p) for p in low_points}

print("Part Two:", np.product(list(map(len,sorted(basins.values(), key=len)[-3:]))))

