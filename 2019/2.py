from handy import *

prog = list(map(int, read(2)[0].split(',')))


def run(n, v, prog):
    ctr = 0
    prog = prog.copy()
    prog[1] = n 
    prog[2] = v

    while prog[ctr] != 99:
        a = prog[prog[ctr+1]]
        b = prog[prog[ctr+2]]
        if prog[ctr] == 1:
            prog[prog[ctr+3]] = a + b
        elif prog[ctr] == 2:
            prog[prog[ctr+3]] = a * b
        else:
            raise Exception()
        ctr += 4
    return prog[0]

res = False
for n in range(100):
    for v in range(100):
        if run(n, v, prog) == 19690720:
            res = True
            print(n,v,100*n+v)
            break
    if res:
        break
