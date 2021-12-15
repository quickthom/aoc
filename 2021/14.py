from handy import read, read_test

lines = read(14)
#lines = read_test(14)
pattern, r = lines[0], lines[2:]

rules = {pair:pair[0]+ins for pair, ins in [x.split(' -> ') for x in r]}
from itertools import product


def expand(pattern, rules, step=1):

    def expands(pattern, rules, step=1):
        out = []
        for i in range(0,len(pattern)-1,step):
            out.append(rules[pattern[i:i+step+1]])
        return "".join(out)+pattern[-1]
    if len(pattern) > 100:
        br = len(pattern)//2
        a = expand(pattern[:br],rules,step)
        b = expand(pattern[br:],rules,step)
        btw = rules[a[-1]+b[0]]
        return a[:-1]+btw+b
    else:
        return expands(pattern,rules,step)

from collections import Counter,defaultdict

for i in range(10):
    print(i)
    pattern = expand(pattern,rules)

counts = Counter(pattern)
print(max(counts.values())-min(counts.values()))

rules3={"".join(p):expand("".join(p),rules)[:-1] for p in
        product(list(counts.keys()),repeat=3)}
rules4={"".join(p):expand("".join(p),rules)[:-1] for p in
        product(list(counts.keys()),repeat=4)}
rules5={"".join(p):expand("".join(p),rules)[:-1] for p in
        product(list(counts.keys()),repeat=5)}
rules3.update(rules)
rules4.update(rules3)
rules5.update(rules4)

#for i in range(40):
#    print(i)
#    pattern = expand(pattern,rules6,5)
#counts = Counter(pattern)
#print(max(counts.values())-min(counts.values()))
pattern = lines[0]
rules = {pair:ins for pair, ins in [x.split(' -> ') for x in r]}
expansions = dict()
for pair, ins in rules.items():
    expansions[pair] = ([pair[0]+ins,ins+pair[1]], ins)
elem_counts = Counter(pattern)
pair_counts = Counter([pattern[i:i+2] for i in range(len(pattern)-1)])
for k in range(40):
    print(k)
    out = Counter()
    for pair, c in pair_counts.items():
        p, i = expansions[pair]
        for pi in p:
            out[pi] += c
        elem_counts[i] += c
    pair_counts = Counter(out)

print(max(elem_counts.values())-min(elem_counts.values()))

