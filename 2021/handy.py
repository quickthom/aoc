def read(fn):
    with open(f'input/{fn}','r') as f:
        return [x.strip() for x in f.readlines()]
def read_test(fn):
    with open(f'input/{fn}.test','r') as f:
        return [x.strip() for x in f.readlines()]
def read_grid(fn, col_delim=" ", row_delim="\n"):
    with open(f'input/{fn}','r') as f:
        return Grid(f.read(), col_delim=col_delim, row_delim=row_delim)
def read_test_grid(fn, col_delim=" ", row_delim="\n"):
    with open(f'input/{fn}.test','r') as f:
        return Grid(f.read(), col_delim=col_delim, row_delim=row_delim)

E = enumerate

class Grid:
    def __init__(self, data, col_delim=" ", row_delim="\n", dtype=int):
        if col_delim is not None and col_delim != "":
            self.lines = [[dtype(y.strip()) for y in x.split(col_delim)] for x
                    in data.strip().split(row_delim)]
        else:
            self.lines = [[dtype(y.strip()) for y in x] for x in
                    data.strip().split(row_delim)]

        self.width, self.height = len(self.lines[0]), len(self.lines)

    def show(self):
        for line in self.lines:
            print(line)
    def scan(self):
        return [(r,c) for r in range(self.height) for c in range(self.width)]

    def get_4_neighbors(self,r,c):
        adj = [(r-1,c  ),
               (r,  c-1),(r,  c+1),
               (r+1,c  )]
        return [(r,c) for r,c in adj if r >=0 and c>=0 and r<self.height and c<self.width]
    def get_8_neighbors(self,r,c):
        adj = [(r-1,c  ),(r-1,c-1),(r-1,c+1),
               (r,  c-1),(r,  c+1),
               (r+1,c  ),(r+1,c-1),(r+1,c+1)]
        return [(r,c) for r,c in adj if r >=0 and c>=0 and r<self.height and c<self.width]

    def apply(self, fn, coords=None):
        if coords is None:
            for r in range(self.height):
                    self.lines[r] = list(map(fn,self.lines[r]))
        else:
            for r,c in coords:
                self.lines[r][c] = fn(self.lines[r][c])

    def __getitem__(self, args):
        if len(args) == 1:
            if isinstance(args[0], int):
                return self.lines[args[0]]
            else:
                return self.lines[args[0][0]][args[0][1]]
        else:
            return self.lines[args[0]][args[1]]
            
    def __setitem__(self, key, value):
        self.lines[key[0]][key[1]] = value
        
