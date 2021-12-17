from handy import *
import numpy as np
from numpy import flip
from collections import defaultdict
from cv2 import matchTemplate as cv2m

with open('input/20') as f: inp = f.read()
#with open('input/20.test') as f: inp = f.read()

raw = dict()

for chunk in inp.strip().split('\n\n'):
    lines = chunk.strip().split('\n')
    n = int(lines[0].split()[1][:-1])
    a = np.array(list(map(lambda x: list(map(lambda y: 1 if y=='#' else 0,
        x)),lines[1:])))
    raw[n] = a  

borders = {n:{tuple(a[0,:]), tuple(a[:,0]), tuple(a[-1,:]), tuple(a[:,-1]),
              tuple(flip(a[0,:])), tuple(flip(a[:,0])),
              tuple(flip(a[-1,:])), tuple(flip(a[:,-1]))   } 
            for n,a in raw.items()}

matches = []
img_matches = defaultdict(int)
for n, b in borders.items():
    for n2, b2 in borders.items():
        if n == n2:
            continue
        if (isect := len(b & b2)) > 0:
            matches.append((n, n2, isect))
            img_matches[n] += isect

corners = sorted(img_matches.keys(), key=lambda x: img_matches[x])[:4]
print(corners, np.product(corners))

def transform(img):
    for hflip in range(2):
        img = flip(img,0)
        for vflip in range(2):
            img = flip(img, 1)
            for rot in range(4):
                img = flip(img.T, 1)
                yield img

oriented = dict()
def search_pattern(tiles, pattern, where='left'):
    for n in tiles:
        for img in transform(raw[n]):
            if where == 'left':
                if tuple(img[:,0]) == tuple(pattern):
                    oriented[n] = img
                    return n
            if where == 'up':
                if tuple(img[0,:]) == tuple(pattern):
                    oriented[n] = img
                    return n

    return None

def orient_top_left_corner(n, img):
    tiles = set(raw.keys())
    tiles.remove(n)
    right = img[:,-1]
    down = img[-1, :]
    while (search_pattern(tiles, right, 'left') is None) or (search_pattern(tiles,down,'up')) is None:
        img = flip(img.T, 1)
        right = img[:,-1]
        down = img[-1, :]
    return img
    
grid_size = int(len(raw)**0.5)
tiles = np.zeros((grid_size, grid_size))

tiles[0][0] = corners[0]
oriented[corners[0]] = orient_top_left_corner(corners[0], raw[corners[0]])

# Do top row
r = 0
for c in range(grid_size-1):
    tile = tiles[r,c]
    if tile == 0: raise Exception()
    right = oriented[tile][:,-1]
    remaining = [x for x in raw.keys() if x not in tiles]
    img = search_pattern(remaining, right, 'left')
    tiles[r, c+1] = img

for r in range(grid_size-1):
    for c in range(grid_size):
        tile = tiles[r,c]
        if tile == 0: raise Exception()
        down = oriented[tile][-1,:]
        remaining = [x for x in raw.keys() if x not in tiles]
        tiles[r+1, c] = search_pattern(remaining, down, 'up')

rows =[]
for r in range(grid_size):
    rows.append(np.concatenate([oriented[tiles[r,c]][1:-1,1:-1] for c in
        range(grid_size)],1))

final = np.concatenate(rows,0)

monster = """00000000000000000010
10000110000110000111
01001001001001001000"""

m_ovly = np.array([list(x) for x in monster.split('\n')]).astype('uint8')

for final in transform(final):
    monsters = 0
    for r in range(len(final) - len(m_ovly)-2):
      for c in range(len(final[0]) - len(m_ovly[0])):
        if m_ovly.sum() == np.logical_and(
                m_ovly, final[r:r+len(m_ovly), c:c+len(m_ovly[0])]
              ).sum():
              monsters += 1
    if monsters > 0:
        print(monsters, 'monsters')
        print('chop=', final.sum() - (m_ovly.sum())*monsters)
        break




