import requests
import os

cookie = {
    'session':'53616c7465645f5f0dd6697f2a8fada40e904fd407fa090c6dd5c2c5c714b5d6bf83ed0b32ce816a06c146d380a41d7a306cb17275cb3ac94a914d902ef52690'
}

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
       
class Node:
    all_nodes = dict()

    def __init__(self, coord):
        self.coord = coord

    def up(self):
        if self.coord[0] == 0:
            return None
        else:
            return self.all_nodes[(self.coord[0]-1,self.coord[1])]

    def down(self):
        if self.coord[0] >= maxrow:
            return None
        else:
            return self.all_nodes[(self.coord[0]+1,self.coord[1])     ]

    def left(self):
        if self.coord[1] == 0:
            return None
        else:
            return self.all_nodes[(self.coord[0],self.coord[1]-1)      ]
    def right(self):
        if self.coord[1] >= maxcol:
            return None
        else:
            return self.all_nodes[(self.coord[0],self.coord[1]+1)]
                           