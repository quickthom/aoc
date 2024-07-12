import time
from cmn import loadfile, preproc
import math
import pandas as pd
import numpy as np
data = loadfile('day9.txt', 'https://adventofcode.com/2023/day/9/input')

sample = '''
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''
# data = preproc(sample)

def extrap(seq):
    seqs = [seq]
    while sum(seq) != 0:
        seq = np.diff(seq)
        seqs.append(list(seq))
    next_add = 0
    for seq in reversed(seqs):
        seq.append(seq[-1] + next_add)
        next_add = seq[-1]
    return next_add

extrapolated_values = [extrap(list(map(int,x.split()))) for x in data]
print(sum(extrapolated_values))
# 1684566095 - correct

def lextrap(seq):
    seqs = [seq]
    while sum(seq) != 0:
        seq = np.diff(seq)
        seqs.append(list(seq))
    next_add = 0
    for seq in reversed(seqs):
        seq = [seq[0] - next_add] + seq
        next_add = seq[0]
    return next_add

extrapolated_values = [lextrap(list(map(int,x.split()))) for x in data]
print(sum(extrapolated_values))
# 1136