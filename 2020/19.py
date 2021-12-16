from handy import *
from itertools import chain

lines = read(19)
#lines = read_test(19)
k = lines.index('')
t1, t2 = lines[:k], lines[k+1:]

ruletxt = {int(x): y for x,y in [z.split(': ') for z in t1]}

def cross(a, b):
    if not a:
        return b
    if not b:
        return a
    return {ai+bi for ai in a for bi in b}

def process_rule(txt):
    if txt == "42 | 42 8":
        txt = "42 | 42 42" 
    elif txt == "42 31 | 42 11 31":
        txt = "42 31 | 42 42 31 31"
    if '"' in txt:
        return {txt[1:-1]}
    elif '|' in txt:
        return set(chain(*map(process_rule, txt.split(' | '))))
    else:
        out = []
        rules = list(reversed([int(x) for x in txt.split()]))
        while rules:
            out = cross(out, process_rule(ruletxt[rules.pop()]))
        return out

#ruletxt[8] = "42 | 42 8"
#ruletxt[11] = "42 31 | 42 11 31"
r42 = process_rule(ruletxt[42])
r31 = process_rule(ruletxt[31])
r11 = process_rule(ruletxt[11])
r0 = process_rule(ruletxt[0])
r3131 = process_rule("31 31")
r4242 = process_rule("42 42")

extras = 0
z = len(r31.copy().pop())
def ok_so_far(m):
    m31s = []
    m42s = []
    m11s = []
    for i in range(0, len(m), z):
        if m[i:i+2*z] in r11:
            m11s.append(i)
    if not m11s: return False
    if len(m11s) > 1:
        return False
    for i in range(0, len(m), z):
        if m[i:i+z] in r31:
            m31s.append(i)
    if not m31s: return False
    if len(m31s) > 1:
        m11 = min(m11s)
        if m11 < z:
            return False
#        print(m, m11, m[:m11]+' '+m[m11+10:])
        return ok_so_far(m[:m11]+m[m11+2*z:])
    
    for i in range(0, len(m), z):
        if m[i:i+z] in r42:
            m42s.append(i)
    if len(m42s) < 2: return False
    if len(m42s) > 2:
        return ok_so_far(m[z:])
    if min(m31s) < 2*z:
        return False
    if len(m) > 24:
        return False
#    print('31:',m31s)
#    print('11:',m11s)
#    print('42:',m42s)
    assert m42s+m11s+m31s == [0, z, z, 2*z]
    assert len(m) == 3*z
    if m in r0:
        return True
    return False


for m in set(t2) & process_rule(ruletxt[0]):
    print(m)
winners = set(t2) & process_rule(ruletxt[0])
for m in set(t2) - process_rule(ruletxt[0]):
    if ok_so_far(m):
        print(m)
        extras += 1
        winners.add(m)
print(len(set(t2) & process_rule(ruletxt[0])))
print(extras)
print(len(winners))
