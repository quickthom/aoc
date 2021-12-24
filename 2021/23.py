from handy import *

lines = read(23)
#lines = read_test(23)

rooms = {'a':(11,12),'b':(13,14),'c':(15,16),'d':(17,18)}
hallway = list(range(0,11))
bottoms = [12, 14, 16, 18]
tops = [11, 13, 15, 17]
entries = {'a':2, 'b':4, 'c':6, 'd':8}
exits = {11: 2, 13:4, 15:6, 17:8}
energies = {'a':1,'b':10,'c':100,'d':1000}
enters = {v:k for k,v in exits.items()}
exits.update({k+1:v for k,v in exits.items()})
friends = "ABCDabcd"
solved = "...........aabbccdd"
best_g = 999999
def move(amap, states, energy):
    global best_g
    moves = set()
    best_energy = best_g
    if amap.lower() == solved:
        print(energy)
        best_g = min(energy,best_g)
        return energy
    for c in friends:
        moves |= get_moves(amap, c)
    for c, target, steps, priority in moves.copy():
        if priority:
            moves = [(c, target, steps, priority)]
            break
    for c, target, steps, _ in moves:
        newmap = make_move(amap, c, target)
        newenergy = steps * energies[c.lower()] + energy 
        if newenergy > best_g:
            continue
        if newmap.lower() in states and states[newmap.lower()] <= newenergy:
            continue
        states[newmap.lower()] = newenergy
        best_energy = min(best_energy, move(newmap, states, newenergy))
    return best_energy

def make_move(amap, c, target):
    amap = amap.replace(c, '.')
    amap = amap[:target] + c + amap[target+1:]
    return amap

def get_moves(amap, c):
    loc = amap.find(c)
    out = set()
    # If it's already in place, return nothing.
    if loc == rooms[c.lower()][1]:
        return out
    if loc == rooms[c.lower()][0] and amap[rooms[c.lower()][1]] == c.lower():
        return out
    # If it's blocked in, return nothing.
    if loc in bottoms and amap[loc-1] != '.':
        return out
    
    # If it can slot into the right place, that's the only move.
    if amap[rooms[c.lower()][1]].lower() in ('.',c.lower()):
        target = rooms[c.lower()][0] if amap[rooms[c.lower()][1]] != '.' else rooms[c.lower()][1]
        steps = find_path(amap, c, target)
        if steps > 0:
            return {(c, target, steps, True)}
    # Otherwise, we list all the possible hallway moves.
    for h in hallway:
        s = find_path(amap, c, h)
        if s > 0: out.add((c, h, s, False))
    return out

def find_path(amap, c, target):
    if target in entries.values():
        return 0
    if amap[target] != '.':
        return 0
    loc = amap.find(c)
    steps = 0
    if loc in bottoms:
        loc -= 1
        steps += 1
    if loc in tops:
        loc = exits[loc]
        steps += 1
    if target in hallway:
        hall_tgt = target
    else:
        hall_tgt = exits[target]
    direc = 1 - 2*(hall_tgt < loc)
    while loc != hall_tgt:
        if amap[loc+direc] != '.':
            return 0
        else:
            loc += direc
            steps += 1
    if target == hall_tgt:
        return steps
    else:
        loc = enters[loc]
        steps += 1
    if loc == target:
        return steps
    else:
        return steps+1
    


    

amap = "."*11+lines[2][3]+lines[3][1]+lines[2][5]+lines[3][3]+lines[2][7]+lines[3][5]+lines[2][9]+lines[3][7]

for c in 'ABCD':
    i = amap.find(c)
    amap = amap[:i]+c.lower()+amap[i+1:]

states = dict()
energy = 0
