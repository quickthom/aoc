from handy import *

ms = list(map(int, read(1)))

def fuel(m):
    return max(0, m // 3 - 2)
         
def totfuel(m):
    req = fuel(m)
    tot = req   
    while (req:=fuel(req)) > 0:
        tot += req
    return tot


print(sum([totfuel(x) for x in ms]))

