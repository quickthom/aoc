import time
import re
from itertools import product
from cmn import NodeGrid, Node, loadfile, preproc, print_2D_data, transpose
import pandas as pd
import numpy as np
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
from multiprocessing import Pool

data = loadfile("day15.txt", "https://adventofcode.com/2023/day/15/input")

sample = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""
# data = preproc(sample)
print_2D_data(data)


def hash(s):
    ret = 0
    for c in s:
        ret += ord(c)
        ret = (ret * 17) % 256
    return ret

data = "".join(data)
steps = data.split(",")
print("Total:", sum((hash(step) for step in steps)))


def parse_step(s):
    s = s.strip()
    if s[-1] == "-":
        lbl = s[:-1]
        foc = None
    else:
        foc = int(s[-1])
        lbl = s[:-2]
    box = hash(lbl)
    return box, lbl, foc


class Box:
    def __init__(self, n):
        self.n = n
        self.lenses = list()

    def remove_lens(self, lbl):
        for i, lens in enumerate(self.lenses):
            if lens[0] == lbl:
                self.lenses.pop(i)
                break

    def has_lens(self, lbl):
        return any((lens[0] == lbl for lens in self.lenses))

    def find_lens(self, lbl):
        for i, lens in enumerate(self.lenses):
            if lens[0] == lbl:
                return i
        return -1

    def __repr__(self):
        return str(self.lenses)

    def add_lens(self, lbl, foc):
        i = self.find_lens(lbl)
        if i > -1:
            self.lenses[i] = (lbl, foc)
        else:
            self.lenses.append((lbl, foc))

    def power(self):
        return sum(
            ((i + 1) * foc * (self.n + 1) for i, (lbl, foc) in enumerate(self.lenses))
        )


boxes = {i: Box(i) for i in range(256)}

if __name__ == "__main__":
    for step in steps:
        box, lbl, foc = parse_step(step)
        b = boxes[box]
        if foc is None:
            b.remove_lens(lbl)
        else:
            b.add_lens(lbl, foc)

for i in (0, 1, 3):
    print(i, boxes[i])
print(sum((b.power() for b in boxes.values())))
