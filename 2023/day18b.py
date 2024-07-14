import types
import time
import re
from itertools import product
from cmn import NodeGrid, Node, loadfile, preproc, print_2D_data, transpose, is_not_none
import pandas as pd
import numpy as np
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
from multiprocessing import Pool

data = loadfile("day18.txt", "https://adventofcode.com/2023/day/18/input")

sample = r"""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""
data = preproc(sample)
G = NodeGrid(data)

d_code_map = "RDLU"

# r = 223
# c = 68
# marks = [(223,68)]
r = 0
c = 0
marks = [(0,0)]
for d, n, col in [x.split() for x in data]:
    n = int(col[-7:-2], 16)
    d = d_code_map[int(col[-2])]
    for i in range(int(n)):
        if d == 'R':
            c += 1
        elif d == 'L':
            c -= 1
        elif d == 'U':
            r -= 1
        elif d == 'D':
            r += 1
        else:
            raise NotImplementedError()
        marks.append((r,c))

maxr = max((x[0] for x in marks))
minr = min((x[0] for x in marks))
maxc = max((x[1] for x in marks))
minc = min((x[1] for x in marks))

G = NodeGrid([""])
G.maxrow, G.maxcol, G.ncols, G.nrows = maxr, maxc, maxc-minc+1, maxr-minr+1
for i in range(minr,maxr+1):
    for j in range(minc,maxc+1):
        n = Node((i,j))
        G.nodes[(i,j)] = n
        if (i,j) in marks:
            n.value = '#'
        else:
            n.value = '.'
        n.holds_lava = False
        n.grid = G
        n.all_nodes = G.nodes
G.print()

# interior_point = (258,5)
interior_point = (1,1)
nodes_to_fill = [G.loc(*interior_point)]

while len(nodes_to_fill) > 0:
    node = nodes_to_fill.pop()
    node.holds_lava = True
    if node.value == '#':
        for exit in node.exits():
            if exit.value == '#' and not exit.holds_lava:
                nodes_to_fill.append(exit)
    else:
        for exit in node.exits():
            if not exit.holds_lava:
                nodes_to_fill.append(exit)
            
sum((n.holds_lava for n in G.nodes.values()))
