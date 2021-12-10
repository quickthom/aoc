import numpy as np
import pandas as pd
from handy import read

lines = read(7)

positions = pd.Series([int(x) for x in lines[0].split(',')])
#positions = pd.Series([16,1,2,0,4,2,7,1,2,14])


low_pos = min(positions)
hi_pos = max(positions)

best_pos = -1
best_fuel = 0
for pos in range(low_pos+1, hi_pos):
    fuel = (positions - pos).abs().sum()
    if best_pos < 0 or best_fuel > fuel:
        best_pos = pos
        best_fuel = fuel
print("Align at position",best_pos,"using", best_fuel,"fuel")

max_dist = hi_pos - low_pos
fuel_costs = np.array(list(range(max_dist))).cumsum()

best_pos = -1
best_fuel = 0
for pos in range(low_pos+1, hi_pos):
    diffs = (positions - pos).abs()
    fuel = fuel_costs[diffs].sum()
    if best_pos < 0 or best_fuel > fuel:
        best_pos = pos
        best_fuel = fuel
print("Align at position",best_pos,"using", best_fuel,"fuel")
