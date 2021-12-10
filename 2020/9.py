from handy import read
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from itertools import combinations

lines = [int(x) for x in read(9)]

def validate(n, last):
    last = set((x for x in last if x <= n))
    for combo in combinations(last, 2):
        if sum(combo) == n:
            return True
    return False

invalid = 0
for i in range(25, len(lines)):
    if not validate(lines[i], lines[i-25:i]):
        print('Not valid:',lines[i])
        invalid = lines[i]

for window_shape in range(2,100):
  window_sums = np.sum(sliding_window_view(lines, window_shape = window_shape), axis = 1)
  if invalid in window_sums:
      print('Located, window size', window_shape)
      ix = np.where(window_sums==invalid)[0][0]
      window = sliding_window_view(lines, window_shape = window_shape)[ix]
      print(min(window)+max(window))

  

