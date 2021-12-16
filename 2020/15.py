from handy import *
from collections import defaultdict

lines = read(15)
#lines = read_test(15)

numbers = dict()

for i,n in E(lines[0].split(',')):
    numbers[int(n)] = i
def play(numbers, i, n):
    if n in numbers:
        out = i - numbers[n]
    else:
        out = 0
    numbers[n] = i
    return out
last = int(n)
for i in range(i,30000000-1):
    last = play(numbers, i, last)
    if i > 29990000:
        print(last)
