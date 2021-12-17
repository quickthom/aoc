from handy import *

inp = read(17)[0]
#inp = read_test(17)[0]

_, inp = inp.split(': ')
inpx, inpy = inp.split(', ')
xrng = tuple(map(int, inpx[2:].split('..')))
yrng = tuple(map(int, inpy[2:].split('..')))
xrng = (xrng[0], xrng[1]+1)
yrng = (yrng[0], yrng[1]+1)

def shoot(xv, yv):
    x,y = (0,0)
    peaky = 0
    for _ in range(10000):
        if y > peaky:
            peaky = y
        if x in range(*xrng) and y in range(*yrng):
            return peaky
        if x >= xrng[1]:
            return -100
        if y < yrng[0]:
            return -100
        x += xv
        y += yv
        if xv > 0:
            xv -= 1
        yv -= 1

scores = dict()
for xv in range(500):
    for yv in range(-500,500):
        scores[(xv, yv)] = shoot(xv, yv)

print(max(scores.values()))
print(len(list(filter(lambda x: x >-100, scores.values()))))
