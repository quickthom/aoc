import time
import re
from itertools import product
from cmn import loadfile, preproc, print_2D_data
import pandas as pd
import numpy as np
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
from multiprocessing import Pool

data = loadfile("day13.txt", "https://adventofcode.com/2023/day/13/input")

sample = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
# data = preproc(sample)
# print_2D_data(data)


def parse_data(data):
    data = data + [""]
    ret = []
    while "" in data:
        try:
            bp = data.index("")
            ret.append(data[:bp])
            data = data[bp + 1 :]
        except:
            break
    return ret


samples = parse_data(data)


def find_identical_rows(data):
    ret = []
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            ret.append(i)
    return ret


def find_identical_columns(data):
    return find_identical_rows(transpose(data))

def transpose(data):
    return ["".join(x) for x in np.array([list(x) for x in data]).T]
def mirrorcheck(sample, row):
    top = row
    btm = row + 1
    while top >= 0 and btm < len(sample):
        if not sample[top] == sample[btm]:
            return False
        top -= 1
        btm += 1
    return True
    
scores = []
for sample in samples:
    for r in find_identical_rows(sample):
        if mirrorcheck(sample, r):
            scores.append(100 * (r+1))
    for c in find_identical_columns(sample):
        if mirrorcheck(transpose(sample), c):
            scores.append(c +1)

print(sum(scores))

newscores = []
flip = {'#':'.', '.':'#'}
def do_flip(data, r, c):
    row = data[r]
    new_row = row[:c]+flip[row[c]]+row[c+1:]
    data[r] = new_row
    return data

if __name__=='__main__':
    for sample_i, sample in enumerate(samples):
        oldscore = scores[sample_i]
        found = False
        for i in range(len(sample)):
            for j in range(len(sample[0])):
                if not found:
                    do_flip(sample, i, j)
                    for r in find_identical_rows(sample):
                        if mirrorcheck(sample, r):
                            if 100*(r+1) != oldscore:
                                found = True
                                newscores.append(100 * (r+1))
                    for c in find_identical_columns(sample):
                        if mirrorcheck(transpose(sample), c):
                            if c+1 != oldscore:
                                found = True
                                newscores.append(c + 1)
                    do_flip(sample, i, j)

print(sum(newscores))
