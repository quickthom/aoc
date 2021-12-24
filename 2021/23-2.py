from handy import *

lines = read(23)
#lines = read_test(23)

rooms = {'A':(11,12,13,14),'B':(15,16,17,18),'C':(19,20,21,22),'D':(23,24,25,26)}
hallway = list(range(0,11))
bottoms = [14, 18, 22, 26]
wells = [12,13,14,16,17,18,20,21,22,24,25,26]
tops = [11, 15, 19, 23]
entries = {'A':2, 'B':4, 'C':6, 'D':8}
unstoppables = set(entries.values())
old_exits = {11: 2, 15:4, 19:6, 23:8}
energies = {'A':1,'B':10,'C':100,'D':1000}
enters = {v:k for k,v in old_exits.items()}
exits = old_exits.copy()
exits.update({k+1:v for k,v in old_exits.items()})
exits.update({k+2:v for k,v in old_exits.items()})
exits.update({k+3:v for k,v in old_exits.items()})
solved = "...........AAAABBBBCCCCDDDD"
best_g = 9952596
bestgame = None

def friends(amap):
    return (x for x in range(len(amap)) if amap[x] != '.')

def move(amap, states, energy,game,last_move=0):
    global best_g,bestgame
    moves = set()
    best_energy = best_g
    if amap == solved:
        print(energy)
        best_g = min(energy,best_g)
        if best_g == energy:
            bestgame = game
        return energy
    for loc in friends(amap):
        if loc != last_move:
            moves |= get_moves(amap, loc)
    for loc, target, steps, priority in moves.copy():
        if priority:
            moves = [(loc, target, steps, priority)]
            break
    for loc, target, steps, _ in moves:
        if amap[target] != '.':
            continue
        newmap = amap[:target] + amap[loc] + amap[target+1:]
        newmap = newmap[:loc] + '.' + newmap[loc+1:]
        c = amap[loc]
        newenergy = steps * energies[c] + energy 
        if newenergy > best_g:
            continue
        if newmap in states and states[newmap] <= newenergy:
            continue
        states[newmap] = newenergy
        newgame = game.copy()
        newgame.append((loc, target, steps, newenergy))
        best_energy = min(best_energy, move(newmap, states, newenergy,newgame,target))
    return best_energy

def make_move(amap, loc, target):
    newmap = amap[:target] + amap[loc] + amap[target+1:]
    newmap = newmap[:loc] + '.' + newmap[loc+1:]
    return newmap


def get_moves(amap, loc):
    c = amap[loc]
    out = set()
    # If it's blocked in, return nothing.
    if loc in wells and amap[loc-1] != '.':
        return out
    # If it's already in place, return nothing.
    if loc in rooms[c]:
        if all([amap[x] in ('.',c) for x in rooms[c]]):
            return out
    # If it can slot into the right place, that's the only move.
    if all([amap[x] in ('.',c) for x in rooms[c]]):
        target = rooms[c][-1]
        while amap[target] != '.':
            target -= 1
        steps = find_path(amap, loc, target)
        if steps > 0:
            return {(loc, target, steps, True)}
    # Otherwise, we list all the possible hallway moves.
    if loc not in hallway:
        for h in hallway:
            s = find_path(amap, loc, h)
            if s > 0: out.add((loc, h, s, False))
    return out

def find_path(amap, loc, target):
    if target in unstoppables:
        return 0
    if amap[target] != '.':
        return 0
    c = amap[loc]
    steps = 0
    while loc in wells:
        loc -= 1
        if amap[loc] != '.':
            return 0
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
        if amap[loc] != '.':
            return 0
        steps += 1
    while loc < target:
        loc += 1
        if amap[loc] != '.':
            return 0
        steps += 1
    return steps
    


    

amap = "."*11+lines[2][3]+'DD'+lines[3][1]+lines[2][5]+'CB'+lines[3][3]+lines[2][7]+'BA'+lines[3][5]+lines[2][9]+'AC'+lines[3][7]

for c in 'ABCD':
    i = amap.find(c)
    amap = amap[:i]+c+amap[i+1:]

states = dict()
energy = 0
game = []
move(amap, states, energy,game)
print(bestgame)
print(states[solved])
