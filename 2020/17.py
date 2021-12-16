
from handy import read,read_test
import numpy as np
from collections import defaultdict

lines = read_test(17)
lines = read(17)

irows,icols = len(lines),len(lines[0])
rlo,rhi = (0,irows)
clo,chi = (0,icols)
zlo,zhi = (0,1)
wlo,whi = (0,1)

states = defaultdict(int)
for r in range(rlo,rhi):
    for c in range(clo,chi):
        states[(r,c,0,0)] = lines[r][c]=='#'

def render(states):
    for z in range(zlo,zhi):
        print('z=',z)
        for r in range(rlo,rhi):
            for c in range(clo,chi):
                print('#' if states[(r,c,z)] else '.',end='')
            print('')

def get_neighbor_states(r,c,z,w,states):
  out = 0
  for nr in range(r-1,r+2):
      for nc in range(c-1,c+2):
          for nz in range(z-1,z+2):
              for nw in range(w-1,w+2):
                if (nr,nc,nz,nw) != (r,c,z,w):
                  out += int(states[(nr,nc,nz,nw)])
  return out

def iterate(states):
    global rlo,rhi,clo,chi,zlo,zhi,wlo,whi
    rlo,rhi = rlo-1, rhi+1
    clo,chi=clo-1,chi+1
    zlo,zhi=zlo-1,zhi+1
    wlo,whi=wlo-1,whi+1
    newstate = states.copy()
    for r in range(rlo,rhi):
        for c in range(clo,chi):
            for z in range(zlo,zhi):
                for w in range(wlo,whi):
                  if states[(r,c,z,w)] and not get_neighbor_states(r,c,z,w,states) in (2,3):   
                      newstate[(r,c,z,w)] = False
                  elif get_neighbor_states(r,c,z,w,states) == 3:
                      newstate[(r,c,z,w)] = True
    return newstate
for i in range(6):
    states = iterate(states)
print(sum(states.values()))
