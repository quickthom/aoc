
from handy import read

alphabet = set("abcdefghijklmnopqrstuvwxyz")

lines = read(6)
"""lines = [
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b"]"""
groups = [alphabet.copy()]
for line in lines:
    if line == "":
        groups.append(alphabet.copy())
    else:
        groups[-1] = groups[-1].intersection(set(line))

print(sum(map(len, groups)))
