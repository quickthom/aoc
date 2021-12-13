from handy import read
import numpy as np

lines = read(13)

coords, folds = lines[:lines.index('')], lines[lines.index('')+1:]
coords = [(int(r),int(c)) for c,r in [x.split(',') for x in coords]]
folds = [x.split('=') for x in [fold.split()[-1] for fold in folds]]

width = max([c for r,c in coords])+1
height = max([r for r, c in coords])+1

grid = np.zeros([height, width]).astype('bool')

for r, c in coords:
    grid[r, c] = True

for ax, n in folds:
    crease = int(n)
    overlay = np.zeros_like(grid).astype(bool)
    if ax == 'y':
        overlay_height = len(grid) - crease - 1
        overlay[crease-overlay_height:crease, :] =np.flip(grid[crease+1:,:], axis=0)
        grid = (grid | overlay)[:crease,:]

    else:
        overlay_width = len(grid[0]) - crease - 1
        overlay[:,crease-overlay_width:crease] = np.flip(grid[:,crease+1:], axis=1)
        grid = (grid | overlay)[:,:crease]

print(grid.sum())
print('\n'.join([' '.join(['#' if x == 1 else "." for x in z]) for z in
    grid]))
