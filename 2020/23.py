from handy import *
from collections import deque

cups = [int(x) for x in read(23)[0]]
#cups = [int(x) for x in read_test(23)[0]]
nex = max(cups)+1
adds =int(1e6 - len(cups))
cups = cups +list(range(nex,nex+adds))
maxcups = max(cups)

cupref = dict()

class Cup:
    def __init__(self,value):
        self.value = value
        self.next = None
    def link(self, cup):
        cup.next = self
    def popoff(self, n):
        out = []
        cup = self
        for i in range(n):
            out.append(cup)
            cup = cup.next
        return out

startcup = lc = Cup(cups[0])
cupref[startcup.value] = startcup
for i in cups[1:]:
    c = Cup(i)
    cupref[i] = c
    c.link(lc)
    lc = c
c.next = startcup

cur = startcup
for i in range(10000000):
    if i % 100000 == 0:
        print(i//1000, ',000')
    cur, *extract, cur.next = cur.popoff(5)
    dest = cur.value
    while dest in [cur.value]+[x.value for x in extract]:
        dest -= 1
        if dest < 1: dest = maxcups
    destcup = cupref[dest]
    extract[-1].next = destcup.next
    destcup.next = extract[0]
    cur = cur.next
cup = cupref[1].next
for _ in range(2):
    print(cup.value,end=',')
    cup = cup.next
