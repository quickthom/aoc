from handy import *
from fractions import Fraction
import numpy as np


e_departure, bustxt = read_test(13)
e_departure, bustxt = read(13)

buses = [int(x) for x in bustxt.split(',') if x != 'x']
bus = 0
depart = 0
for i in range(int(e_departure),int(e_departure)*2):
    for b in buses:
        if i % b == 0:
            depart = i
            bus = b
            break
    if bus >0:
        break

wait = i- int(e_departure)
print(f'Bus={bus} Arrive={e_departure} Depart={depart} Wait={wait}')
print(bus * wait)

offsets = dict()
first_bus = int(bustxt.split(',')[0])
for i, bus in enumerate(bustxt.split(',')):
    if bus != 'x':
        offsets[int(bus)] = i

max_bus, max_offset = max(offsets.keys()), offsets[max(offsets.keys())]

sorted_buses = sorted(offsets.keys(), reverse=True)

tfirst = 0
start = 1#100000000000000
step = 1
for j in range(1,len(offsets)+1):
    tfirst = 0
    for i in range(start,start*1000,step):
        t = i
        for k,v in list(offsets.items())[0:j]:
            if (i+v) % k != 0:
                t = 0
                break
        if t > 0: 
            if tfirst == 0:
                tfirst = t
                t = 0
            else:
                break
    step = t-tfirst
    start = t
    print(tfirst,start, step)
