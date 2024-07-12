import time
import re
from itertools import product
from cmn import loadfile, preproc, print_2D_data
import math
import pandas as pd
import numpy as np
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
from multiprocessing import Pool

data = loadfile("day12.txt", "https://adventofcode.com/2023/day/12/input")

sample = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
# data = preproc(sample)
# print_2D_data(data)

pattern = re.compile(f"#+")
pattern2 = re.compile(f"[\?#]+")

def is_valid(s, counts):
    runs = pattern.findall(s)
    if len(runs) != len(counts):
        return False
    return all((len(runs[i]) == counts[i] for i in range(len(runs))))

cases = dict()
def find_valid_solutions(s, counts,placements=list()):
    if counts not in cases:
        cases[counts] = dict()
    if s not in cases[counts]:    
        if len(counts) == 0:
            # print(placements)
            if '#' in s:
                return 0
            else:
                return 1
        if len(s) < (sum(counts)+len(counts)-1):
            return 0
        if s.count('?')+s.count('#') < sum(counts):
            return 0
        n = counts[0]
        arrangements = 0
        for slot in find_slots(s, n):
            # if len(s) - slot - n - 1 < sum(counts[1:]):
            #     continue
            arrangements += find_valid_solutions(s[slot+n+1:], counts[1:])
        cases[counts][s] = arrangements
    return cases[counts][s]

def find_slots(s, n):
    pattern = rf"(?<!#)(?=(.{{{n}}})(?!#))"
    # pattern = rf"(?<!#)([?#]{{{n}}})(?!#)"
    matches = re.finditer(pattern, s)
    if (first_hash := s.find('#')) < 0:
        first_hash = len(s)
    return [match.start() for match in matches if '.' not in match.group(1) and match.start() <= first_hash]
    return [match.start() for match in matches if set(match.group(1)).issubset({'?', '#'}) and match.start() <= first_hash]


# arrangements = 0
# for i, r in enumerate(data):
#     str_springs, str_counts = r.split(" ")
#     counts = list(map(int, str_counts.split(",")))
    
#     tgt_count = sum(counts)
#     mgl_tgt = tgt_count - str_springs.count("#")
#     spring_template = str_springs.replace("?", "%s")
#     n = str_springs.count("?")
#     arr = 0
#     for x in product("#.", repeat=n):
#         if x.count("#") != mgl_tgt:
#             continue
#         s = spring_template % x
#         if is_valid(s, counts):
#             arrangements += 1
#             arr += 1
#     if arr != find_valid_solutions(str_springs, counts):
#         print(str_springs, counts, arr, find_valid_solutions(str_springs, counts))
#         # break
#     if i % 100 == 0:
#         print("*", end="")

# print("", arrangements)
def do_row(r):
    str_springs, str_counts = r.split(" ")
    str_springs = "?".join([str_springs] *5)
    str_counts = ",".join([str_counts] * 5)
    counts = tuple(map(int, str_counts.split(",")))
    return find_valid_solutions(str_springs, counts)

def do():

    arrangements = 0
    begin = time.time()
    for i, r in enumerate(data):
        arrangements += do_row(r)
        if i % 1 == 0:
            print("*", end="")
        if i % 100 == 0:
            elapsed = (time.time() - begin) / 60
            secs = int(100*(elapsed-np.floor(elapsed)))
            t = "%i:%.2i" % (int(np.floor(elapsed)), secs)
            print("\n",t, i, " ", end="")
    print("\nArrangements:",arrangements)

if __name__ == "__main__":
    with Profiler(interval=.01) as prof:
        do()
    print(prof.output(ConsoleRenderer(flat=True)))  
    # pool = Pool(4)
    # with Profiler(interval=.001) as prof:
    #     z=pool.map(do_row, data)
    # print(prof.output(ConsoleRenderer(flat=True)))
    # pool.close()
    # print("\nArrangements:",sum(z))


# with Profiler(interval=.001) as prof:
#     s= '??????????????????????????????????????????????????????'
#     s = s#[:-11]
#     c = (1,1,4,1,1,4,1,1,4,1,1,4,1,1,4)
#     c = c#[:-3]
#     find_valid_solutions(s,c)
# print(prof.output(ConsoleRenderer(flat=True)))

# with Profiler(interval=.001) as prof:
#     s= '?.???????.???????.???????.???????.???????.???????.???????.???????.???????.?????'
#     s = s[:-15]
#     c = (1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2)
#     c = c#[:-5]
#     res = find_valid_solutions(s,c)
#     print(res)
# print(prof.output(ConsoleRenderer(flat=True)))
