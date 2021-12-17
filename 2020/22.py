from handy import *

with open('input/22','r') as f: inp = f.read()
#with open('input/22.test','r') as f: inp = f.read()

p1t, p2t = inp.split('\n\n')
p1 = list(reversed([int(x) for x in p1t.strip().split('\n')[1:]]))
p2 = list(reversed([int(x) for x in p2t.strip().split('\n')[1:]]))
depth = 0
def play(p1,p2):
    global depth
    depth += 1
    memories = set()
    def simulate(p1,p2):
        c1, c2 = p1.pop(), p2.pop()
        if len(p1) >= c1 and len(p2) >= c2:
            winner, score = play(p1.copy()[-c1:], p2.copy()[-c2:])
        else:
            winner = 1 + (c2 > c1)
        if winner == 1:
            p1 = [c2, c1] + p1
        else:
            p2 = [c1, c2] + p2
        return p1, p2

    while len(p1) * len(p2) > 0:
        if (tuple(p1), tuple(p2)) in memories:
            break
        else:
            memories.add((tuple(p1), tuple(p2)))
            p1, p2 = simulate(p1, p2)
    
    if len(p1)*len(p2) > 0:
        winner = 1
        win = p1
    else:
        winner = 1 if len(p1) != 0 else 2
        win = p1 if len(p1) != 0 else p2
    if depth < 2:
        score = sum([(i+1)*card for i, card in enumerate(win)])
    else:
        score = 0
    depth -= 1
#    print(depth)
    return winner, score

