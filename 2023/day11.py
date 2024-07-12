import time
from cmn import loadfile, preproc
import math
import pandas as pd
import numpy as np
data = loadfile('day11.txt', 'https://adventofcode.com/2023/day/11/input')

sample = '''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''
# data = preproc(sample)

rowcount = len(data)
colcount = len(data[0])
maxrow = rowcount - 1
maxcol = colcount - 1
expansion_cols = []
expansion_rows = []

out = []
for r, row in enumerate(data):
    out.append(row)
    if all([i == '.' for i in row]):
        # out.append(row)
        expansion_rows.append(r)

transposed_data = [''.join(x) for x in np.array([list(x) for x in out]).T]
transposed_out = []
for j, row in enumerate(transposed_data):
    transposed_out.append(row)
    if all([i == '.' for i in row]):
        # transposed_out.append(row)
        expansion_cols.append(j)

data = [''.join(x) for x in np.array([list(x) for x in transposed_out]).T]
rowcount = len(data)
colcount = len(data[0])
maxrow = rowcount - 1
maxcol = colcount - 1

class Galaxy:
    def __init__(self, coord):
        self.coord = coord    
    @property
    def row(self):
        return self.coord[0]
    @property
    def col(self):
        return self.coord[1]

galaxies = dict()
for i in range(rowcount):
    for j in range(colcount):
        if data[i][j] == '#':
            galaxies[(i,j)] = Galaxy((i,j))

print(len(galaxies))

def between(n, a, b):
    if a == b:
        return False
    a, b = min(a,b), max(a,b)
    return (n > a) and (n < b)

def distance(g1, g2):
    base_distance = abs(g1.row - g2.row) + abs(g1.col - g2.col)
    for r in expansion_rows:
        if between(r, g1.row, g2.row):
            base_distance += 999999
    for c in expansion_cols:
        if between(c, g1.col, g2.col):
            base_distance += 999999
    return base_distance            

from itertools import combinations
distances = []
galaxy_pairs = combinations(galaxies.values(), 2)
for g1, g2 in galaxy_pairs:
    distances.append(distance(g1,g2))

sum(distances)

# 82,000,210 too low