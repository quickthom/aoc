import types
import time
import re
from itertools import product
from cmn import NodeGrid, Node, loadfile, preproc, print_2D_data, transpose, is_not_none
import pandas as pd
import numpy as np
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
from multiprocessing import Pool

data = loadfile("day18.txt", "https://adventofcode.com/2023/day/18/input")

sample = r"""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""
data = preproc(sample)
G = NodeGrid(data)
G.print()