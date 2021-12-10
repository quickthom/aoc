import pandas as pd
from collections import defaultdict
from handy import read

lines = read(6)

initial_state = list(map(int, lines[0].split(',')))
#initial_state = [3,4,3,1,2]

cohorts = defaultdict(int)
cohorts.update(dict(pd.Series(initial_state).value_counts()))

def rotate(cohorts):
    for i in range(-1, 8):
        cohorts[i] = cohorts[i+1]
    cohorts[6] += cohorts[-1]
    cohorts[8] = cohorts[-1]

for i in range(257):
    if i in (0,2,4,8,16,32,64,80, 128,256):
        print(i, sum(cohorts.values())-cohorts[-1])
    rotate(cohorts)
