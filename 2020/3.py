import numpy as np
from handy import read



def get_tree_count(slope):
    lines = read(3)
    """lines = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
            ]"""
    map_height = len(lines)
    map_target_width = map_height * slope[1] + 1
    while len(lines[0]) < map_target_width:
        for j in range(len(lines)):
            lines[j] += lines[j]
    for i in range(len(lines)):
        lines[i] = list(map(int, lines[i].replace('.','0').replace('#','1')))
    trees = 0
    pos = (0,0)

    while pos[0] < len(lines)-1:
        pos = (pos[0] + slope[0], pos[1] + slope[1])
        trees += lines[pos[0]][pos[1]]
    print('Slope:', slope, 'Trees encountered:', trees)
    return trees

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
print(np.product(list(map(get_tree_count, slopes))))
