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

data = loadfile("day17.txt", "https://adventofcode.com/2023/day/17/input")

sample = r"""
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
# data = preproc(sample)
G = NodeGrid(data)
for n in G.nodes.values():
    n.value = int(n.value)
    n.bests = dict()
    n.bestpaths = dict()
    n.done = False

reverses = dict(up="down", down="up", left="right", right="left")
steps = 0
straights = 0
dest = G.loc(G.maxrow, G.maxcol)


def valid_dirs(moving, straights):
    ret = set(["up", "down", "right", "left"])
    if moving == "x":
        return ret
    else:
        ret.remove(reverses[moving])
        if straights >= 3:
            ret.remove(moving)
    return ret

def valid_dirs(moving, straights):
    ret = set(["up", "down", "right", "left"])
    if moving == "x":
        return ret
    else:
        if straights < 4:
            return set([moving])
        ret.remove(reverses[moving])
        if straights >= 10:
            ret.remove(moving)
    return ret

if __name__ == "__main__":
    nodes_to_do = set([(G.loc(0,0), 'x', 0, 0)])
    distances = []
    best_d = (G.nrows+G.ncols)*6
    while len(nodes_to_do) > 0:
        n, moving, straights, runing = nodes_to_do.pop()
        if n is dest:
            if straights < 4:
                continue
            distances.append(n.value + runing)
            best_d = min(best_d, distances[-1])
        if runing > best_d:
            continue
        exits = {d: n.go(d) for d in valid_dirs(moving, straights) if n.go(d) is not None}
        if (moving, straights) in n.bests and n.bests[(moving, straights)] < n.value + runing:
            continue
        n.bests[(moving, straights)] = n.value + runing
        for d, exit in exits.items():
            nodes_to_do.add((exit, d, 1 if d !=moving else straights+1,n.value + runing))

    print(min(distances)-G.loc(0,0).value)
    # 1064 too low

