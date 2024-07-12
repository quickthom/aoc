import types
import time
import re
from itertools import product
from cmn import NodeGrid, Node, loadfile, preproc, print_2D_data, transpose
import pandas as pd
import numpy as np
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
from multiprocessing import Pool

data = loadfile("day16.txt", "https://adventofcode.com/2023/day/16/input")

sample = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""
# data = preproc(sample)
# print_2D_data(data)
to_exec = list()

def approach_left(self):
    if not self.hit_l:
        self.hit_l = True
        self.energized = True
        if self.value == '.': self.value = '#'
        if self.value in "/|":
            if (n := self.up()) is not None:
                to_exec.add(n.approach_down)
        if self.value in '\|':
            if (n := self.down()) is not None:
                to_exec.add(n.approach_up)
        if self.value in "#.-":
            if (n := self.right()) is not None:
                to_exec.add(n.approach_left)
        

def approach_right(self):
    if not self.hit_r:
        self.hit_r = True
        self.energized = True
        if self.value == '.': self.value = '#'
        if self.value in "\|":
            if (n := self.up()) is not None:
                to_exec.add(n.approach_down)
        if self.value in '/|':
            if (n := self.down()) is not None:
                to_exec.add(n.approach_up)
        if self.value in "#.-":
            if (n := self.left()) is not None:
                to_exec.add(n.approach_right)
def approach_up(self):
    if not self.hit_u:
        self.hit_u = True
        self.energized = True
        if self.value == '.': self.value = '#'
        if self.value in "#.|":
            if (n := self.down()) is not None:
                to_exec.add(n.approach_up)
        if self.value in '/-':
            if (n := self.left()) is not None:
                to_exec.add(n.approach_right)
        if self.value in '\-':
            if (n := self.right()) is not None:
                to_exec.add(n.approach_left)
def approach_down(self):
    if not self.hit_d:
        self.hit_d = True
        self.energized = True
        if self.value == '.': self.value = '#'
        if self.value in "#.|":
            if (n := self.up()) is not None:
                to_exec.add(n.approach_down)
        if self.value in '/-':
            if (n := self.right()) is not None:
                to_exec.add(n.approach_left)
        if self.value in '\-':
            if (n := self.left()) is not None:
                to_exec.add(n.approach_right)

def make_grid(data):
    g = NodeGrid(data)
    for n in g.nodes.values():
        n.energized = False
        n.hit_l = False
        n.hit_r = False
        n.hit_u = False
        n.hit_d = False
        n.approach_down = types.MethodType(approach_down, n)
        n.approach_up = types.MethodType(approach_up, n)
        n.approach_left = types.MethodType(approach_left, n)
        n.approach_right = types.MethodType(approach_right, n)
    return g


G = make_grid(data)
left_edge = [(r, 0) for r in range(G.nrows)]
right_edge = [(r, G.maxcol) for r in range(G.nrows)]
top_edge = [(0, c) for c in range(G.ncols)]
bottom_edge = [(G.maxrow, c) for c in range(G.ncols)]

results = []

print("Left")
for p in left_edge:
    g = make_grid(data)
    to_exec = set([g.nodes[p].approach_left])
    while len(to_exec) > 0:
        to_exec.pop()()
    results.append(sum((n.energized for n in g.nodes.values())))

print("Right")
for p in right_edge:
    g = make_grid(data)
    to_exec = set([g.nodes[p].approach_right])
    while len(to_exec) > 0:
        to_exec.pop()()
    results.append(sum((n.energized for n in g.nodes.values())))

print("Top")
for p in top_edge:
    g = make_grid(data)
    to_exec = set([g.nodes[p].approach_up])
    while len(to_exec) > 0:
        to_exec.pop()()
    results.append(sum((n.energized for n in g.nodes.values())))

print("Bottom")    
for p in bottom_edge:
    g = make_grid(data)
    to_exec = set([g.nodes[p].approach_down])
    while len(to_exec) > 0:
        to_exec.pop()()
    results.append(sum((n.energized for n in g.nodes.values())))

print(max(results))