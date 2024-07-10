
from cmn import loadfile, preproc
import math
data = loadfile('day3.txt', 'https://adventofcode.com/2023/day/3/input')

sample = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''
# data = preproc(sample)

def loc(i, j):
    if i < 0:
        return '.'
    if i >= len(data):
        return '.'
    if j < 0:
        return '.'
    if j >= len(data[0]):
        return '.'
    return data[i][j]

def is_sym(word):
    if len(word) != 1:
        raise Exception("Bad input to is_sym")
    return word not in '0123456789.'

def is_gear(i,j):
    return loc(i,j)=='*'

adjacency = list()
for i in range(len(data)):
    adjacency.append(list())
    for j in range(len(data[1])):
        if (   is_sym(loc(i, j)) 
            or is_sym(loc(i, j-1))
            or is_sym(loc(i, j+1))
            or is_sym(loc(i-1, j))
            or is_sym(loc(i-1, j+1))
            or is_sym(loc(i-1, j-1))
            or is_sym(loc(i+1, j))
            or is_sym(loc(i+1, j+1))
            or is_sym(loc(i+1, j-1))
        ):
            adjacency[-1].append(True)
        else:
            adjacency[-1].append(False)
max_j = len(data[0])
out = []

for i in range(len(data)):
    j = 0
    while j < max_j:
        while not loc(i,j).isnumeric():
            j += 1
            if j > max_j: 
                break
        num = loc(i,j)
        if not num.isnumeric():
            break
        adj = adjacency[i][j]
        while loc(i, j+1).isnumeric():
            num += loc(i,j+1)
            adj = adj or adjacency[i][j+1]
            j += 1
        if adj:
            out.append(int(num))
        j += 1
print(sum(out))

gears = [(i,j) for j in range(len(data[0])) for i in range(len(data)) if loc(i,j) == '*']
gear_friends = {gear: [] for gear in gears}

for i in range(len(data)):
    j = 0
    while j < max_j:
        while not loc(i,j).isnumeric():
            j += 1
            if j > max_j: 
                break
        num = loc(i,j)
        if not num.isnumeric():
            break
        distances = {gear: math.dist(gear, (i, j)) for gear in gears}
        
        while loc(i, j+1).isnumeric():
            num += loc(i,j+1)
            distances = {gear: min(d, math.dist(gear, (i, j+1))) for gear, d in distances.items()}
            j += 1
        for gear in gears:
            if distances[gear] < 1.5:
                gear_friends[gear].append(int(num))
        j += 1
res = 0
for gear, friends in gear_friends.items():
    if len(friends) == 2:
        res += math.prod(friends)
print(res)