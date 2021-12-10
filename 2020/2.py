import pandas as pd
from handy import read

lines = read(2)

def validate(line):
    t1, password = line.split(': ')
    rng, ltr = t1.split()
    low, high = map(int,rng.split('-'))
    ct = (pd.Series(list(password))==ltr).sum()
    return low <= ct <= high

print( sum(map(validate, lines)))

def revalidate(line):
    t1, password = line.split(': ')
    rng, ltr = t1.split()
    pos1, pos2 = map(int,rng.split('-'))
    return ((password[pos1-1] == ltr) + (password[pos2-1] == ltr)) == 1
print( sum(map(revalidate, lines)))
