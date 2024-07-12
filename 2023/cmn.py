import requests
import os

from session import cookie

def loadfile(f, url):
    f = 'inputs/'+f
    if not os.path.isfile(f):
        response = requests.get(url,cookies=cookie)
        if response.status_code == 200:
            with open(f, 'wb') as file:
                file.write(response.content)
        else:
            raise Exception("Failed to get remote file")
        print("Successful retrieval of remote file.")
    with open(f,'r') as file:
        return [line.strip() for line in file.readlines()]

def preproc(data):
    return [d.strip() for d in data.strip().split('\n') if (d is not None)]

def print_2D_data(data):
    dwidth = len(data[0])
    print("    1234567890 13 16  20   25"[:dwidth+4])
    print('    '+'-'*dwidth)
    for i in range(len(data)):
        print(i, end=" | ")
        for j in range(dwidth):
            print(data[i][j], end="")
        print("")
       
def transpose(data):
    return ["".join(x) for x in np.array([list(x) for x in data]).T]

class NodeGrid:
    def __init__(self, data):
        self.nrows = len(data)
        self.ncols = len(data[0])
        self.maxrow = self.nrows-1
        self.maxcol = self.ncols-1
        self.nodes = dict()
        for r,c in self.all_points():
            n = Node((r,c))
            n.value = data[r][c]
            n.grid = self
            n.all_nodes = self.nodes
            self.nodes[(r,c)] = n


    def all_points(self):
        from itertools import product
        return product(range(self.nrows),range(self.ncols))

    def print(self):
        dwidth = self.ncols
        print("    1234567890 13 16  20   25"[:dwidth+4])
        print('    '+'-'*dwidth)
        for i in range(self.nrows):
            print(i, end=" | ")
            for j in range(dwidth):
                print(self.nodes[(i,j)].value, end="")
            print("")
     
        
        
class Node:

    def __init__(self, coord):
        self.coord = coord
        self.value = None
        self.all_nodes = dict()
        self.grid = None
        self._up = ...
        self._down = ...
        self._left = ...
        self._right = ...

    def up(self):
        if self._up is ...:

            if self.coord[0] == 0:
                self._up = None
            else:
                self._up = self.all_nodes[(self.coord[0]-1,self.coord[1])]

        return self._up

    def down(self):
        if self._down is ...:
            if self.coord[0] >= self.grid.maxrow:
                self._down = None
            else:
                self._down =  self.all_nodes[(self.coord[0]+1,self.coord[1])     ]
        return self._down

    def left(self):
        if self._left is ...:
            if self.coord[1] == 0:
                self._left = None
            else:
                self._left = self.all_nodes[(self.coord[0],self.coord[1]-1)      ]
        return self._left

    def right(self):
        if self._right is ...:
            if self.coord[1] >= self.grid.maxcol:
                self._right = None
            else:
                self._right = self.all_nodes[(self.coord[0],self.coord[1]+1)]
        return self._right
                               
