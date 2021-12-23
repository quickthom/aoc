from handy import *
from scipy.spatial import distance
from collections import defaultdict
from itertools import combinations, product

lines = read(19)
#lines = read_test(19)

class Scanner:
    def __init__(self, n):
        self.n = n
        self.orient = (0,1,2)
        self.reflect = (1,1,1)
        self._points = set()
        self.translate = (0,0,0)
        self.oriented = False

    def reorient(self, orient, reflect):
        orient_map = {self.orient[i]:orient[i] for i in range(len(orient))}
        reflect_map = [self.reflect[i]*reflect[i] for i in range(len(reflect))]
        self.orient = orient
        self.reflect = reflect_map

    def add(self, point):
        self._points.add(point)

    @property
    def points(self):
        xi, yi, zi = self.orient
        xr, yr, zr = self.reflect
        points = {(v[xi]*xr, v[yi]*yr, v[zi]*zr) for v in self._points}
        xt, yt, zt = self.translate
        return {(x+xt, y+yt, z+zt) for x,y,z in points}

    def distances(self):
        ds = defaultdict(list)
        for p1, p2 in combinations(self.points, 2):
            ds[p1].append(distance.euclidean(p1,p2))
            ds[p2].append(distance.euclidean(p1,p2))
        return {k:sorted(v) for k,v in ds.items()}

        

scanners = []
for line in lines:
    if 'scanner' in line:
        n = int(line.split()[-2])
        scanner = Scanner(n)
        scanners.append(scanner)
    elif ',' in line:
        scanner.add(tuple(map(int, line.split(','))))

def overlaps(s1, s2):
    d1 = s1.distances()
    d2 = s2.distances()
    out = []
    out2 = []
    for k1, k2 in product(d1.keys(), d2.keys()):
        p1 = d1[k1]
        p2 = d2[k2]
        if len(set(p1) & set(p2)) > 9:
            out.append((k1, k2))
            out2.append((sum(k1),sum(k2)))
    return out,out2

def orient(s1, s2):
    for reflect in product((-1,1),(-1,1),(-1,1)):
        for orient in permutations((0,1,2),3):
            s1.reflect = reflect
            s1.orient = orient
            s1.translate = (0,0,0)
            x, y = overlaps(s1,s2)
            a, b, c = x[0][0]
            a2, b2, c2 = x[0][1]
            a0, b0, c0 = s1.translate
            s1.translate = (a0-a+a2,b0-b+b2,c0-c+c2)
            x, y = overlaps(s1,s2)
            totdist =[distance.euclidean(*z) for z in x]
#            print(totdist)
            if sum(totdist) == 0:
                s1.oriented = True
                return True
    raise Exception('Could not orient.')

def n_overlaps(s1, s2):
    x, y = overlaps(s1, s2)
    return len(x)

def orient_scanners(scanners):
    scanners[0].oriented = True
    for s in scanners[1:]:
        if s.oriented:
            continue
        else:
            for sbase in scanners:
                if not sbase.oriented:
                    continue
                if s.n == sbase.n:
                    continue
                if n_overlaps(s, sbase) >= 12:
                    print(s.n, sbase.n)
                    try:
                      orient(s, sbase)
                      break
                    except:
                      continue
while sum([x.oriented for x in scanners]) < len(scanners):
    orient_scanners(scanners)
print(len(set.union(*[x.points for x in scanners])))

def manhattan(s1, s2):
    p1 = map(abs, s1.translate)
    p2 = map(abs, s2.translate)
    return sum(p1)+sum(p2)

biggest_d = 0
for s1, s2 in combinations(scanners, 2):
    x1, y1, z1 = s1.translate
    x2,y2,z2 = s2.translate
    d = sum(map(abs, [x2-x1, y2-y1, z2-z1]))
    if d > biggest_d:
        biggest_d = d
        print(d)

