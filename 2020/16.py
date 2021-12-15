from handy import *
import pandas as pd
import numpy as np
from itertools import chain
from collections import defaultdict

lines = read(16)
#lines = read_test(16)
s1, s2, s3 = '\n'.join(lines).split('\n\n')

rules = dict()
for line in s1.split('\n'):
    vname, rest = line.split(': ')
    rules[vname] = list(chain(*[list(range(int(a),int(b)+1))
                    for a,b in [x.split('-') 
                    for x in rest.split(' or ')]]))

def split_ticket(x): return [int(y) for y in x.split(',')]
ticket0 = split_ticket(s2.split('\n')[1])
tickets = list(map(split_ticket, s3.split('\n')[1:])) + [ticket0]

all_valid = set()
for rule in rules.values():
    all_valid = all_valid | set(rule)

def invalid(x): return x not in all_valid
print(sum([sum(filter(invalid,ticket)) for ticket in tickets]))

tickets = pd.DataFrame([t for t in tickets if not any(map(invalid,t))])
poss = defaultdict(set)
for v, rules in rules.items():
    for c in tickets.columns:
        if tickets[c].isin(rules).all():
            poss[v].add(c)

while max(map(len, poss.values())) > 1:
    for v, p in poss.copy().items():
        if len(p) == 1:
            for v_, p_ in poss.items():
                if v_ != v:
                    poss[v_] = p_ - p
    
tickets.columns = sorted(poss.keys(), key=lambda x: poss[x].pop())
print(tickets[tickets.columns[tickets.columns.str.startswith('departure')]].iloc[-1].product())
