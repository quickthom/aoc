from handy import *
import numpy as np
from scipy.sparse import coo_matrix
from collections import defaultdict
from itertools import combinations

lines = read(22)
lines = read_test(22)

slices = []

defaultdictlist = lambda: defaultdict(list)
cube = defaultdict(defaultdictlist)
tot = 0
for line in lines:
    on_off = line.split()[0] == 'on'
    xt, yt, zt = [tuple(map(int,x[2:].split('..'))) for x in line[3:].strip().split(',')]
    slices.append((on_off, xt,yt,zt))
    if on_off:
        tot += (xt[1]-xt[0])*(yt[1]-yt[0])*(zt[1]-zt[0])

overlaps = []
for a,b in combinations(slices,2):
    if a[0] != b[0]:
        ax, ay, az = a[1:]
        bx, by, bz = b[1:]
        if ax[0] > bx[1] or bx[0] > ax[1]:
            continue
        if ay[0] > by[1] or by[0] > ay[1]:
            continue
        if az[0] > bz[1] or bz[0] > az[1]:
            continue
        overlaps.append((a,b))

tot = 0
for x in range(-100000,100000):
    print('x=',x)
    for y in range(-100000,100000):
        print('y=',y)
        for z in range(-100000,100000):
            mark = 0
            for on, (xlo,xhi),(ylo,yhi),(zlo,zhi) in slices:
                if x > xhi or x < xlo:
                    continue
                if y > yhi or y < ylo:
                    continue
                if z > zhi or z < zlo:
                    continue
                mark = on
            tot += mark
                
