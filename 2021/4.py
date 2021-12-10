import numpy as np
from handy import read

data = read(4)
"""data = [
"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
"",
"22 13 17 11  0",
" 8  2 23  4 24",
"21  9 14 16  7",
" 6 10  3 18  5",
" 1 12 20 15 19",
"",
" 3 15  0  2 22",
" 9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
" 2  0 12  3  7"]"""

called_numbers = [int(x) for x in data[0].split(',')]

class BingoBoard:
    def __init__(self, data, n):
        self.rows = []
        self.columns = []
        self.rep = []
        self.n = n

        for row_ in data:
            row = [int(x) for x in row_.split()]
            self.rows.append(row)
            self.rep.append(row.copy())
        arr = np.array(self.rows)
        self.columns = [list(x) for x in arr.T]
        self.won = False
    def __repr__(self):
        out = ""
        for row in range(5):
            for col in range(5):
                if self.rep[row][col] not in self.rows[row]:
                    out = out + '*'
                out= out + str(self.rep[row][col]) +' '
            out += '\n'
        return out
    def mark(self, number):
        for r in self.rows:
            if number in r:
                r.remove(number)
        for c in self.columns:
            if number in c:
                c.remove(number) 
    def check(self):
        lengths = [len(x) for x in self.rows+self.columns]
        return min(lengths) <= 0
    def score(self, last_call):
        base = sum([sum(x) for x in self.rows])
        return base * last_call

boards = []
for i in range(2, len(data), 6):
    boards.append(BingoBoard(data[i:i+5],len(boards)))

winners = []
if True:
    for n in called_numbers:
        players = [b for b in boards if not b.won]
        if len(players) == 0:
            break
        for i, board in enumerate(players):
            board.mark(n)
            if board.check():
                print(f'Board {board.n} wins! Last called: {n}. Final Score:', board.score(n))
                winners.append((board.n, board.score(n)))
                board.won = True
