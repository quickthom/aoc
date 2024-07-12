import time
import re
from itertools import product
from cmn import NodeGrid,Node,loadfile, preproc, print_2D_data,transpose
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
        mp ={'O':3,'#':7000,'.':5000003}
        ret = 0
        for (r,c), n in self.nodes.items():
            ret += mp[n.value]*(r+c*100)
        return ret
    def north_weight(self):
        R = self.nrows
        return sum([R-r for (r,c),n in self.nodes.items() if n.value=='O'])
    def tilt_up(self):
        return self.tilt('up')

    def tilt(self, direction):
      for r in range(self.nrows):
        for c in range(self.ncols):
          n = self.nodes[(r,c)]
          nxt = n
          if n.value == 'O':
              n2=None
              while True:
                  nxt = nxt.__getattribute__(direction)()
                  if nxt is None:
                      break
                  if nxt.value != '.':
                      break
                  n2=nxt

              if n2 is not None and n2.value =='.':
                  n2.value = 'O'
                  n.value = '.'
    def cycle(self,dxn):
        last = self.hash()
        self.tilt(dxn)
        while G.hash() != last:
            last = G.hash()
            self.tilt(dxn)


if __name__=='__main__':
    G = Grid(data)
#    G.print()
    gohash = G.hash()
    hashes = dict()
    gowt = G.north_weight()
    hashing = True
    shish=[G.north_weight()]
    wt=0
    for i in range(1000000000):
        if hashing:
          go = G.hash()
          if go in hashes:
              hashing=False
              go,wt = hashes[go]
          else:
            G.cycle('up')
            G.cycle('left')
            G.cycle('down')
            G.cycle('right')
            hashes[go] = (G.hash(),G.north_weight())
            shish.append(G.north_weight())
        else:
          break
          go,wt = hashes[go]

    h = gohash
    rec = []
    while h not in rec:
        rec.append(h)
        h,w = hashes[h]
    spot = rec.index(hashes[h][0])
    rec.append(hashes[h][0])
    travel = len(rec)-1-spot
    wrap = rec[spot:-1] 
    def w_at_iter(i):
        if i < spot:
            raise Exception()
        i = i - spot
        ix = i % travel
        return hashes[wrap[ix]]

print(w_at_iter(1000000001))
#95868 too high
