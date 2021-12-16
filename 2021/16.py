from handy import *
import numpy as np

def unhex(c):
    b = bin(int(c, base=16))[2:]
    while len(b) < 4*len(c):
        b = "0" + b
    return b

def bint(x): return int(x, base=2)

def bexs(x, n): 
    return ''.join([x.pop() for i in range(n)])
def bex(x, n): return bint(bexs(x,n))

class Packet:
    def __init__(self, vers, typ):
        self.vers = vers
        self.typ = typ
        self.val = None
        self.subs = []

    def extract_literal(self, b):
        xtract = ""
        while b:
            more = bex(b, 1)
            xtract += bexs(b, 4)
            if not more:
                break
        self.val = bint(xtract)

    def __repr__(s): return f'V:{s.vers} T:{s.typ} Subs:{len(s.subs)} Value:{s.val}'

    def calculate(self):
        for sub in self.subs:
            sub.calculate()
        if self.typ == 0:
            self.val = sum([x.val for x in self.subs])
        elif self.typ == 1:
            self.val = np.product([x.val for x in self.subs])
        elif self.typ == 2:
            self.val = min([x.val for x in self.subs])
        elif self.typ == 3:
            self.val = max([x.val for x in self.subs])
        elif self.typ == 5:
            self.val = int(self.subs[0].val > self.subs[1].val)
        elif self.typ == 6:
            self.val = int(self.subs[0].val < self.subs[1].val)
        elif self.typ == 7:
            self.val = int(self.subs[0].val == self.subs[1].val)
        return self.val

def parse(b, loops=1):
    global vsum
    out = []
    for i in range(loops):
        if not b: break
        v, t = bex(b, 3), bex(b, 3) # Header
        vsum += v
        p = Packet(v,t)
        if t == 4:
            p.extract_literal(b)
        else:
            if bex(b,1) == 0:
                p.subs = parse(list(reversed(bexs(b, bex(b,15)))),1000)
            else:
                p.subs = parse(b, bex(b, 11))
        out.append(p)
    return out

hx = read(16)[0]
b = list(reversed(unhex(hx)))

vsum = 0
top = parse(b)[0]
print('Part 1:', vsum, 'Part 2:', top.calculate())

