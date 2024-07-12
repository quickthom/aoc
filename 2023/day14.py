import time
import re
from itertools import product
from cmn import NodeGrid, Node, loadfile, preproc, print_2D_data, transpose
import pandas as pd
import numpy as np
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
from multiprocessing import Pool

data = loadfile("day14.txt", "https://adventofcode.com/2023/day/14/input")

sample = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
# data = preproc(sample)
# print_2D_data(data)


class Grid(NodeGrid):
    def hash(self):
        # ret = []
        # for r in range(self.nrows):
        #     for c in range(self.ncols):
        #         ret.append(self.nodes[(r,c)].value)
        # return "".join(ret)
        mp = {"O": 3, "#": 7000, ".": 5000003}
        ret = 0
        for (r, c), n in self.nodes.items():
            ret += mp[n.value] * (r + c * 100)
        return ret

    def north_weight(self):
        R = self.nrows
        return sum([R - r for (r, c), n in self.nodes.items() if n.value == "O"])

    def tilt_up(self):
        return self.tilt("up")

    def tilt(self, direction):
        for r in range(self.nrows):
            for c in range(self.ncols):
                n = self.nodes[(r, c)]
                nxt = n
                if n.value == "O":
                    n2 = None
                    while True:
                        nxt = nxt.__getattribute__(direction)()
                        if nxt is None or nxt.value != ".":
                            break
                        n2 = nxt

                    if n2 is not None and n2.value == ".":
                        n2.value = "O"
                        n.value = "."

    def cycle(self, dxn):
        last = self.hash()
        self.tilt(dxn)
        while G.hash() != last:
            last = G.hash()
            self.tilt(dxn)


if __name__ == "__main__":
    G = Grid(data)
    #    G.print()
    gohash = G.hash()
    hashes = dict()
    weights = dict()
    gowt = G.north_weight()
    hashing = True
    shish = [G.north_weight()]
    states = dict()
    wt = 0
    cycles_run = 0
    go = gohash
    for i in range(1000000000):
        if go not in hashes:
            weights[go] = G.north_weight()
            G.cycle("up")
            G.cycle("left")
            G.cycle("down")
            G.cycle("right")
            hashes[go] = go = G.hash()
            states[go] = [cycles_run+1]
        else:
            go = hashes[go]
        cycles_run += 1
        states[go].append(cycles_run)
        history = states[go]
        if len(history) > 0:
            delta = history[-1] - history[-2]
            if cycles_run + delta < 1000000000:
                cycles_run += delta
            states[go].append(cycles_run)
        if i % 10 == 0:
            print(f'i={i} cycles_run={cycles_run}')
        if cycles_run == 1000000000:
            print(weights[go])
            break
print(cycles_run)
