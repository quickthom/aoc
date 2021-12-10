import numpy as np
from handy import read

lines = [int(x) for x in read(10)]
#lines = [16, 10 ,15 ,5 ,1 ,11 ,7 ,19 ,6, 12, 4]
#lines = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3,]
chargers = np.array(sorted(lines+[0]+[max(lines)+3]))
diffs = np.diff(chargers)
final = max(chargers)

cache = dict()
def count_arrangements(start, chargers):
  if start in cache:
      return cache[start]
  if start == final:
      return 1
  branches = chargers[((chargers - start) <= 3) & ((chargers-start)>0)]
  if len(branches) == 0:
      cache[start] = 0
      return 0
  else:
      cache[start] = sum((count_arrangements(x, chargers[chargers>=x]) for x in branches))
      return cache[start]
