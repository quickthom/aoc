import pandas as pd
from handy import read

h = 0
d = 0
lines = read(2)
for line in lines:
    cmd, i = line.split()
    if cmd == 'forward':
        h += int(i)
    elif cmd == 'down':
        d += int(i)
    elif cmd == 'up':
        d -= int(i)
print(f'x={h}, depth={d}')

h=0
d=0
aim = 0
for line in lines:
    cmd, i = line.split()
    if cmd == 'forward':
        h += int(i)
        d += int(i) * aim
    elif cmd == 'down':
        aim += int(i)
    elif cmd == 'up':
        aim -= int(i)
print(f'x={h}, depth={d}, prod={h*d}')
