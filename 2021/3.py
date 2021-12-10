import pandas as pd
from handy import read
from collections import defaultdict

lines = read(3)
def maxes(lines, flip=False):
    counter = [0]*(len(lines[0]))

    for line in lines:
        for i in range(len(line)):
          counter[i] += int(line[i])
    
    thresh = len(lines) / 2
    if flip:
        ones = pd.Series(counter)>thresh
    else:
        ones = pd.Series(counter)>=thresh
    zeros = ~ones
    return ones, zeros

gammad, epsd = maxes(lines)

gammab = ''.join(list(gammad.astype(int).astype(str)))
epsb = ''.join(list(epsd.astype(int).astype(str)))

gamma = int(gammab, base=2)
eps = int(epsb, base=2)

print(f'epsilon={eps}, gamma={gamma}, prod={eps*gamma}')

def filt(ls, digit, val):
    return [x for x in ls if x[digit]==str(int(val))]

oxys = lines
for i in range(len(oxys[0])):
    oxys = filt(oxys, i, maxes(oxys)[0][i])
    if len(oxys) <= 1:
        break
oxy = int(oxys[0], base=2)

co2s = lines
for i in range(len(co2s[0])):
    co2s = filt(co2s, i, maxes(co2s,False)[1][i])
    if len(co2s) <= 1:
        break
co2 = int(co2s[0], base=2)

print(f'oxygen={oxy}, CO2={co2}, prod={oxy*co2}')
