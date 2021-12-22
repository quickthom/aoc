from handy import *
import re
from itertools import permutations
import numpy as np

lines = read(18)
#lines = read_test(18)

#int = lambda x: int(x, base=16)
def remap_regnums(n, regnums):
    for i in range(99,-1,-1):
        n = n.replace(str(i), '%i')
    return n % tuple(regnums)

def is_flat_pair(n):
    if n[0] != '[':
        return 0
    i = 0
    while n[i+1] != ']':
        i += 1
    if '[' in n[1:i+1]:
        return 0
    else:
        return i+1

def find_explosion(n):
    global regnums
    opens = 0
    regnums = list(map(int,n.replace('[','').replace(']','').split(',')))
    regnums_idx = -1
    for i,c in E(n):
        if c in '0123456789':
            if n[i+1] not in '0123456789':
                regnums_idx += 1
        elif opens > 3 and c == '[':
            if (i2:=is_flat_pair(n[i:])):
                # Explode
                    if regnums_idx > -1:
                        regnums[regnums_idx] += regnums[regnums_idx+1]
                    if regnums_idx + 3 < len(regnums):
                        regnums[regnums_idx+3] += regnums[regnums_idx+2]
                    regnums = regnums[:regnums_idx+1] + [0] + regnums[regnums_idx+3:]
                    newn = n[:i]+'0'+n[i+i2+1:]
#                    n = remap_regnums(n.replace(n[i:i+i2+1],'0'), regnums)
                    n = remap_regnums(newn, regnums)
                    break
            else:
                opens += 1
        elif c == '[':
            opens += 1
        elif c == ']':
            opens -= 1
        elif c == ',':
            pass
    return n

def find_split(s):
    regnums = list(map(int,s.replace('[','').replace(']','').split(',')))
    for i,n in E(regnums):
        if n > 9:
            ix = s.find(str(n))
            ln = len(str(n))
            a = int(n // 2)
            b = int(np.ceil(n/2))
            s = s[:ix] + f'[{a},{b}]'+s[ix+ln:]
            break
    return s

def do_solving(s):
    done = False
    last = s
    while find_split(find_explosion(s)) != s:
        s = find_explosion(s)
        if s == last:
            s = find_split(s)
        last = s
    return s

s = lines[0]
line = lines[1]
print(f'[{s},{line}]')
for line in lines[1:]:
    s = do_solving(f'[{s},{line}]')
    print(s)

inn = re.compile("\[\d+,\d+\]")
def calc_magnitude(s):
    if inn.findall(s)[0] == s:
        a, b = map(int,s[1:-1].split(','))
        return a*3 + b*2
    else:
        for a in inn.findall(s):
            s = s.replace(a, str(calc_magnitude(a)))
        return calc_magnitude(s)
print(calc_magnitude(s))

best_mag = 0
pairs = permutations(lines, 2)
for a, b in pairs:
    s = do_solving(f'[{a},{b}]')
    if (m:=calc_magnitude(s)) > best_mag:
        best_mag = m
        print(m)


