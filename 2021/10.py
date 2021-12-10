from handy import read
import numpy as np

lines = read(10)
"""lines = ["[({(<(())[]>[[{[]{<()<>>",
"[(()[<>])]({[<{<<[]>>(",
"{([(<{}[<>[]}>{[]{[(<()>",
"(((({<>}<{<{<>}{[]{[]{}",
"[[<[([]))<([[{}[[()]]]",
"[{[{({}]{}}([{[{{{}}([]",
"{<[[]]>}<{[{[{[]{()[[[]",
"[<(<(<(<{}))><([]([]()",
"<{([([[(<>()){}]>(<<{{",
"<{([{{}}[<[[[<>{}]]]>[]]"]"""


pairs = {'(':')', "[":"]", "<":">", "{":"}"}
scores = {')':3, "]":57, ">":25137, "}":1197,"(":1,"[":2,"{":3,"<":4}

results = {lnum: 0 for lnum in range(len(lines))}
inc_results = []

for lnum, line in enumerate(lines):
    chunk_stack = list()
    for char in line:
        if char in pairs.keys():
            chunk_stack.append(char)
        elif char in pairs.values():
            if len(chunk_stack) == 0 or pairs[chunk_stack[-1]] != char:
                results[lnum] = scores[char]
                chunk_stack = []
                break
            else:
                chunk_stack = chunk_stack[:-1]
    # score incomplete line
    points = [scores[x] for x in reversed(chunk_stack)]
    inc_score = 0
    for p in points:
        inc_score = inc_score * 5 + p
    inc_results.append(inc_score)

print(sum(results.values()))
print(np.median([x for x in inc_results if x > 0]))



