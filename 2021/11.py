from handy import read, read_test

lines = read(11)
#lines = read_test(11)

class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False
    def increase(self):
        self.energy += 1
        if self.energy > 9:
            if not self.flashed:
                self.flashed = True
                return self.flashed
            else:
                return False
    def reset(self):
        self.energy = 0
        self.flashed = False


octopi = []
for i, line in enumerate(lines):
    octopi.append([Octopus(int(j)) for j in line])


def get_adjacent_octopi(octopi, coords):
    row, col = coords
    adjacents = [(row-1,col),(row-1,col-1),(row-1,col+1),
                 (row, col-1), (row, col+1),
                 (row+1, col-1), (row+1,col), (row+1,col+1)]
    return [(r,c) for r,c in adjacents if r >=0 and c>=0 and r<=9 and c<=9]

def trigger_adjacents(octopi, coords):
    for row, col in get_adjacent_octopi(octopi,coords):
        if octopi[row][col].increase():
            trigger_adjacents(octopi, (row, col))

def simulate(octopi):
    for i,row in enumerate(octopi):
        for j,octopus in enumerate(row):
            if octopus.increase():
                trigger_adjacents(octopi, (i,j))
    flashes = 0
    for i,row in enumerate(octopi):
        for j,octopus in enumerate(row):
            if octopus.flashed:
                flashes += 1
                octopus.reset()
    return flashes

def ostatus(octopi):
    for row in octopi:
        print([x.energy for x in row])

for i in range(10000):
    x = simulate(octopi)
    if x == 100:
        print(i+1)
        break
