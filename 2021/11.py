from handy import read, read_test, E

lines = read(11)
#lines = read_test(11)

class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flash = False
    def inc(self):
        self.energy += 1
        if self.energy > 9:
            if not self.flash:
                self.flash = True
                return self.flash
            else:
                return False
    def reset(self):
        self.energy = 0
        self.flash = False


octopi = [[Octopus(int(j)) for j in line] for line in lines]

def get_adj(row, col):
    adj = [(row-1,col),(row-1,col-1),(row-1,col+1),
                 (row, col-1), (row, col+1),
                 (row+1, col-1), (row+1,col), (row+1,col+1)]
    return [(r,c) for r,c in adj if r >=0 and c>=0 and r<=9 and c<=9]

def trig_adj(o, coords):
    for row, col in get_adj(*coords):
        if octopi[row][col].inc():
            trig_adj(o, (row, col))

def simulate(o):
    for i,row in E(o):
        for j,octo in E(row):
            if octo.inc():
                trig_adj(o,(i,j))
    flashes = 0
    for i,row in E(octopi):
        for j,octo in E(row):
            if octo.flash:
                flashes += 1
                octo.reset()
    return flashes

print(sum([simulate(octopi) for i in range(100)]))

octopi = [[Octopus(int(j)) for j in line] for line in lines]

def ostatus(octopi):
    for row in octopi:
        print([x.energy for x in row])

for i in range(10000):
    x = simulate(octopi)
    if x == 100:
        print(i+1)
        break
