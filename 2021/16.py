from handy import *
import numpy as np

lines = read(16)
hx = lines[0]

def bint(x): return int(x, base=2)
def unhex(c):
    b = bin(int(c, base=16))[2:]
    while len(b) % 4 != 0:
        b = "0" + b
    i = 0
    while c[i] == '0':
        b = "0000" + b
        i += 1
    return b

def bex(x, n):
    return bint(''.join([x.pop() for i in range(n)]))
def bexs(x, n):
    return ''.join([x.pop() for i in range(n)])

class Packet:
    def __init__(self, version, typ):
        self.version = version
        self.typ = typ
        self.literal = None
        self.value = None
        self.subpackets = []
    def extract_literal(self, content):
        xtract = ""
        while content:
            more = bex(content, 1)
            xtract += bexs(content, 4)
            if not more:
                break
        self.literal = bint(xtract)
        self.value = self.literal
        return content
    def __repr__(self):
        if self.typ ==4:
            return f'V:{self.version} Value:{self.value}'
        else:
            return f'V:{self.version} T:{self.typ} Subs:{len(self.subpackets)} Value:{self.value}'
    def calculate(self):
        for sub in self.subpackets:
            sub.calculate()
        if self.typ == 0:
            self.value = sum([x.value for x in self.subpackets])
        elif self.typ == 1:
            self.value = np.product([x.value for x in self.subpackets])
        elif self.typ == 2:
            self.value = min([x.value for x in self.subpackets])
        elif self.typ == 3:
            self.value = max([x.value for x in self.subpackets])
        elif self.typ == 4:
            self.value = self.literal
        elif self.typ == 5:
            self.value = int(self.subpackets[0].value > self.subpackets[1].value)
        elif self.typ == 6:
            self.value = int(self.subpackets[0].value < self.subpackets[1].value)
        elif self.typ == 7:
            self.value = int(self.subpackets[0].value == self.subpackets[1].value)
        return self.value
    

bn = unhex(hx)
b = list(reversed(bn))
vcount = 0
def parse(b, loops=1):
    global vcount
    out = []
    for i in range(loops):
        if not b:
            break
        v = bex(b, 3)
        t = bint(''.join([b.pop() for i in range(3)]))
        vcount += v
        p = Packet(v,t)
        if t == 4:
            b = p.extract_literal(b)
        else:
            lt = bex(b, 1)
            if lt == 0:
                ln = bex(b, 15)
                p.subpackets = parse(list(reversed(bexs(b, ln))),1000)
            else:
                subs = bex(b, 11)
                p.subpackets = parse(b, subs)
        out.append(p)
    return out


