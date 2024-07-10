import time
from cmn import loadfile, preproc
import math
import pandas as pd
import numpy as np
data = loadfile('day6.txt', 'https://adventofcode.com/2023/day/6/input')

sample = '''
Time:      7  15   30
Distance:  9  40  200
'''
# data = preproc(sample)
times = [int(x.strip()) for x in data[0].split(':')[1].split(' ') if len(x) > 0]
distances = [int(x.strip()) for x in data[1].split(':')[1].split(' ') if len(x) > 0]
def run_race(race_time,btn_time):
    if btn_time >= race_time:
        return 0
    return (race_time - btn_time) * btn_time

races = zip(times, distances)
wins = [sum([run_race(time, i) > distance for i in range(time)]) for time, distance in races]
print(np.prod(wins))
# 293,046

T = int(''.join([(x.strip()) for x in data[0].split(':')[1].split(' ') if len(x) > 0]))
D = int(''.join([(x.strip()) for x in data[1].split(':')[1].split(' ') if len(x) > 0]))

new_wins = sum([run_race(T, i) > D for i in range(T)])
print(new_wins)