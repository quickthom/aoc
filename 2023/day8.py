import time
from cmn import loadfile, preproc
import math
import pandas as pd
import numpy as np
import re
data = loadfile('day8.txt', 'https://adventofcode.com/2023/day/8/input')

sample = '''
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''
# sample = '''
# LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)
# '''
sample = '''
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''
# data = preproc(sample)

directions = data[0]

all_nodes = dict()
pattern = re.compile(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)')
def parse_row(row):
    match = pattern.match(row)
    return match.group(1), match.group(2), match.group(3)

class Node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None
    def __repr__(self):
        return f"Node {self.id}"

for node, ldest, rdest in [parse_row(row) for row in data[2:]]:
    if node not in all_nodes:
        all_nodes[node] = Node(node)
    if ldest not in all_nodes:
        all_nodes[ldest] = Node(ldest)
    if rdest not in all_nodes:
        all_nodes[rdest] = Node(rdest)        
    all_nodes[node].left = all_nodes[ldest]
    all_nodes[node].right = all_nodes[rdest]

# current = all_nodes['AAA']
# steps = 0
# while current.id != "ZZZ":
#     for dir in directions:
#         if dir == 'R':
#             current = current.right
#         elif dir == 'L':
#             current = current.left
#         steps += 1
#         if current.id == 'ZZZ':
#             break

# print(steps)

def all_zees(nodes):
    return all([node.id[-1]=='Z' for node in nodes])

currents = [node for node in all_nodes.values() if node.id[-1] == 'A']
steps = 0
while not all_zees(currents):
    for dir in directions:
        for i in range(len(currents)):
            if dir == 'R':
                currents[i] = currents[i].right
            elif dir == 'L':
                currents[i] = currents[i].left
        steps += 1
        if all_zees(currents):
            break

print(steps)