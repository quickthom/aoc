import time
from cmn import loadfile, preproc
import math
import pandas as pd
import numpy as np
data = loadfile('day5.txt', 'https://adventofcode.com/2023/day/5/input')

sample = '''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''
# data = preproc(sample)

def parse_map(rows):
    ret = []
    for row in rows:
        dest, src, lng = map(int, row.split(' '))
        max_src = src + lng - 1
        modifier = dest - src
        ret.append((src, max_src, modifier))
    return ret

def apply_map(map, values):
    ret = []
    for v in values:
        v2 = v
        for lo, hi, mod in map:
            if v >= lo and v <= hi:
                v2 += mod
        ret.append(v2)
    return ret

def parse_data(data):
    mapstore = []
    maps = {}
    for r in reversed(data):
        if 'seeds' in r:
            seed_list = [int(x.strip()) for x in r.split(': ')[1].split()]
        elif 'map:' in r:
            mapname = r.split(' map:')[0]
            maps[mapname] = parse_map(mapstore)
            mapstore = []
        elif len(r.strip()) > 0:
            mapstore = [r]+mapstore
    return seed_list, maps

seeds, maps = parse_data(data)

soils = apply_map(maps['seed-to-soil'], seeds)
fertilizers = apply_map(maps['soil-to-fertilizer'], soils)
waters = apply_map(maps['fertilizer-to-water'], fertilizers)
lights = apply_map(maps['water-to-light'], waters)
temperatures = apply_map(maps['light-to-temperature'], lights)
humidities = apply_map(maps['temperature-to-humidity'], temperatures)
locations = apply_map(maps['humidity-to-location'], humidities)

print("Lowest:", min(locations)) # 579439039

seed_pairs = np.reshape(seeds, [-1, 2])
seed_pairs = [(665347395-1000, 2000, )]
low_loc = 9999999999
low_loc_seed = None

for low_seed, n_seed in seed_pairs:
    seed_chunk = range(low_seed, low_seed+n_seed)
    soils = apply_map(maps['seed-to-soil'], seed_chunk)
    fertilizers = apply_map(maps['soil-to-fertilizer'], soils)
    waters = apply_map(maps['fertilizer-to-water'], fertilizers)
    lights = apply_map(maps['water-to-light'], waters)
    temperatures = apply_map(maps['light-to-temperature'], lights)
    humidities = apply_map(maps['temperature-to-humidity'], temperatures)
    locations = apply_map(maps['humidity-to-location'], humidities)
    if min(locations) < low_loc:
        low_loc = min(locations)
        low_loc_seed = seed_chunk[locations.index(min(locations))]


print("Lowest:", low_loc)
# 7873084
