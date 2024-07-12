import time
from cmn import loadfile, preproc
import math
import pandas as pd
import numpy as np
data = loadfile('day10.txt', 'https://adventofcode.com/2023/day/10/input')

sample = '''
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
'''

# sample = '''
# .....
# .S-7.
# .|.|.
# .L-J.
# .....
# '''
sample = '''
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
'''
sample = '''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
'''

# sample='''
# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# '''
# data = preproc(sample)

maxcol = len(data[0]) - 1
width = maxcol + 1
maxrow = len(data) - 1
height = maxrow + 1
starts = []
import sys
sys.setrecursionlimit(2500)
def connects_to(p):
    r, c = p
    if data[r][c] == 'S':
        return starts
    elif data[r][c] == '|':
        return [(r-1, c), (r+1, c)]
    elif data[r][c] == '-':
        return [(r, c-1), (r, c+1)]
    elif data[r][c] == 'L':
        return [(r-1, c), (r, c+1)]
    elif data[r][c] == 'J':
        return [(r-1, c), (r, c-1)]    
    elif data[r][c] == '7':
        return [(r+1, c), (r, c-1)]   
    elif data[r][c] == 'F':
        return [(r+1, c), (r, c+1)]
    else:
        return []
start = None

for i in range(len(data)):
    for j in range(maxcol+1):
        if data[i][j] == 'S':
            start = (i,j)
for i in range(len(data)):
    for j in range(maxcol+1):
        try:
            if start in connects_to((i,j)):
                starts.append((i,j))
        except:
            pass

class Node:
    def __init__(self, coord):
        self.coord = coord
        self.exits = []
        self.steps = 0
        i,j = coord
        self.symbol = data[i][j]
        self.flooded_se = False
        self.flooded_ne = False
        self.flooded_sw = False
        self.flooded_nw = False

    def up(self):
        if self.coord[0] == 0:
            return None
        else:
            return all_nodes[(self.coord[0]-1,self.coord[1])]

    def down(self):
        if self.coord[0] >= maxrow:
            return None
        else:
            return all_nodes[(self.coord[0]+1,self.coord[1])     ]

    def left(self):
        if self.coord[1] == 0:
            return None
        else:
            return all_nodes[(self.coord[0],self.coord[1]-1)      ]
    def right(self):
        if self.coord[1] >= maxcol:
            return None
        else:
            return all_nodes[(self.coord[0],self.coord[1]+1)]
                       
    def flood_from_ne(self):
        if self.flooded_ne:
            return None
        self.flooded_ne = True
        # self.propagate_from_ne()
        if self.symbol == '.':
            if not self.flooded_se:
                self.flood_from_se()
            if not self.flooded_sw:
                self.flood_from_sw()
            if not self.flooded_nw:
                self.flood_from_nw()
        elif self.symbol == 'L':
            pass
        elif self.symbol == '|':
            self.flood_from_se()
        elif self.symbol == '7':
            if not self.flooded_nw:
                self.flood_from_nw()
            self.flood_from_se()
        elif self.symbol == '-':
            if not self.flooded_nw:
                self.flood_from_nw()
        elif self.symbol == 'F':
            if not self.flooded_nw:
                self.flood_from_nw()        
            if not self.flooded_sw:
                self.flood_from_sw() 
        elif self.symbol == 'J':            
            if not self.flooded_sw:
                self.flood_from_sw()
            self.flood_from_se()
        
    def propagate_from_ne(self):
        if self.up() is not None:
            self.up().flood_from_se()
        if self.right() is not None:            
            self.right().flood_from_nw()

    def flood_from_se(self):
        if self.flooded_se:
            return None
        self.flooded_se = True
        # self.propagate_from_se()
        if self.symbol == '.':
            if not self.flooded_ne:
                self.flood_from_ne()
            if not self.flooded_sw:
                self.flood_from_sw()
            if not self.flooded_nw:
                self.flood_from_nw()
        elif self.symbol == 'L':
            if not self.flooded_nw:
                self.flood_from_nw()
            self.flood_from_sw()
        elif self.symbol == '|':
            if not self.flooded_ne:
                self.flood_from_ne()
        elif self.symbol == '7':
            self.flood_from_ne()
            if not self.flooded_nw:
                self.flood_from_nw()
        elif self.symbol == '-':
            if not self.flooded_sw:
                self.flood_from_sw()
        elif self.symbol == 'F':
            pass 
        elif self.symbol == 'J':            
            if not self.flooded_ne:
                self.flood_from_ne()
            self.flood_from_sw()
    def propagate_from_se(self):
        if self.down() is not None:
            self.down().flood_from_ne()
        if self.right() is not None:
            self.right().flood_from_sw()

    def flood_from_nw(self):
        if self.flooded_nw:
            return None
        self.flooded_nw = True
        # self.propagate_from_nw()
        if self.symbol == '.':
            if not self.flooded_ne:
                self.flood_from_ne()
            if not self.flooded_sw:
                self.flood_from_sw()
            self.flood_from_se()
        elif self.symbol == 'L':
            self.flood_from_se()
            if not self.flooded_sw:
                self.flood_from_sw()
        elif self.symbol == '|':
            if not self.flooded_sw:
                self.flood_from_sw()
        elif self.symbol == '7':
            if not self.flooded_ne:
                self.flood_from_ne()
            self.flood_from_se()
        elif self.symbol == '-':
            if not self.flooded_ne:
                self.flood_from_ne()
        elif self.symbol == 'F':
            if not self.flooded_ne:
                self.flood_from_ne()
            if not self.flooded_sw:
                self.flood_from_sw()
        elif self.symbol == 'J':            
            pass

    def propagate_from_nw(self):
        if self.up() is not None:
            self.up().flood_from_sw()
        if self.left() is not None:
            self.left().flood_from_ne()

    def flood_from_sw(self):
        if self.flooded_sw:
            return None
        self.flooded_sw = True
        # self.propagate_from_sw()
        if self.symbol == '.':
            if not self.flooded_ne:
                self.flood_from_ne()
            if not self.flooded_nw:
                self.flood_from_nw()
            if not self.flooded_se:
                self.flood_from_se()
        elif self.symbol == 'L':
            if not self.flooded_se:
                self.flood_from_se()
            if not self.flooded_nw:
                self.flood_from_nw()
        elif self.symbol == '|':
            if not self.flooded_nw:
                self.flood_from_nw()
        elif self.symbol == '7':
            pass
        elif self.symbol == '-':
            self.flood_from_se()
        elif self.symbol == 'F':
            if not self.flooded_ne:
                self.flood_from_ne()
            if not self.flooded_nw:
                self.flood_from_nw()
        elif self.symbol == 'J':   
            if not self.flooded_se:         
                self.flood_from_se()
            self.flood_from_ne()

    def propagate_from_sw(self):
        if self.down() is not None:
            self.down().flood_from_nw()
        if self.left() is not None:
            self.left().flood_from_se()

    @property
    def flooded(self):
        return self.flooded_se and self.flooded_ne and self.flooded_sw and self.flooded_nw
    def __repr__(self):
        return f"Node {self.coord}"
    



# start_node = Node(start[0])
# start_node.exits = connects_to(start[0])
# all_nodes[start[0]] = start_node


# def read_node(coords, steps=0):
#     if coords not in all_nodes:
#         n = Node(coords)
#         n.exits = connects_to(coords)
#         n.steps = steps
#         all_nodes[coords] = n
#         for exit in n.exits:
#             if exit not in all_nodes:
#                 read_node(exit, steps+1)
# read_node(starts[0])
# step_counts = [a.steps for a in all_nodes.values()]
# print("Max dist:", int(np.ceil(np.median(step_counts))))

pipe_nodes = dict()
nodes_to_add = [(starts[0], 0)]
while len(nodes_to_add) > 0:
    coords, steps = nodes_to_add.pop()
    if coords not in pipe_nodes:
        n = Node(coords)
        n.exits = connects_to(coords)
        n.steps = steps
        pipe_nodes[coords] = n
        for exit in n.exits:
            if exit not in pipe_nodes:
                nodes_to_add.append((exit, steps+1))

step_counts = [a.steps for a in pipe_nodes.values()]
print("Max dist:", int(np.ceil(np.median(step_counts))))

edges = (
    [(0, c) for c in range(maxcol+1)]
    + [(r, 0) for r in range(len(data))]
    + [(len(data)-1, c) for c in range(maxcol+1)]
    + [(r, maxcol) for r in range(len(data))]
)

outside = set((p for p in edges if p not in pipe_nodes.keys()))
to_search = outside.copy()
searched = set()
from itertools import product
all_points = product(range(height),range(width))
all_nodes = pipe_nodes.copy()
for p in all_points:
    if p not in all_nodes:
        all_nodes[p] = Node(p)
        all_nodes[p].symbol = '.'
for p in outside:
    all_nodes[p].flood_from_ne()
    all_nodes[p].flood_from_nw()
    all_nodes[p].flood_from_se()
    all_nodes[p].flood_from_sw()
for n in all_nodes.values():
    if n.flooded_se: n.propagate_from_se()
    if n.flooded_ne: n.propagate_from_ne()
    if n.flooded_nw: n.propagate_from_nw()
    if n.flooded_sw: n.propagate_from_sw()
outside = set((n.coord for n in all_nodes.values() if n.flooded))
bound_points = set(all_nodes.keys()).difference(outside).difference(set(pipe_nodes.keys()))

for i in range(len(data)):
    for j in range(maxcol+1):
        if (i,j) in pipe_nodes:
            print(pipe_nodes[(i,j)].symbol, end="")
        elif (i,j) in outside:
            print("_",end="")
        elif (i,j) in bound_points:
            print("I",end="")            
        else:
            print(" ", end="")
    print("\n")

print(len(bound_points))
#5580 too high