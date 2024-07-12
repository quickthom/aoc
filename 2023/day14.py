import time
import re
from itertools import product
from cmn import loadfile, preproc, print_2D_data
import pandas as pd
import numpy as np
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
from multiprocessing import Pool

data = loadfile("day14.txt", "https://adventofcode.com/2023/day/14/input")

sample = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
# data = preproc(sample)
# print_2D_data(data)
