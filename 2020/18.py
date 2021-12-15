from handy import *

lines = read(18)
#lines = read_test(18)

import re

re_parens = re.compile('(\(([^()]+)\))')
re_plus = re.compile('\d+ \+ \d+')

def calculate(line):
    while len(parens := re_parens.findall(line)) > 0:
        for paren in parens:
            line = line.replace(paren[0], str(calculate(paren[1])))
    line = list(reversed(line.split()))
    while len(line) > 1:
        a = int(line.pop())
        op = line.pop()
        if op == '+':
            line.append(a+int(line.pop()))
        elif op == '*':
            line.append(a*int(line.pop()))
    return line[0]

print(sum([calculate(x) for x in lines]))

def calculate2(line):
    while len(parens := re_parens.findall(line)) > 0:
        for paren in parens:
            line = line.replace(paren[0], str(calculate2(paren[1])))
    while '+' in line:
        adds = re_plus.findall(line)
        for add in adds:
            a,_,b = add.split()
            line = line.replace(add, str(int(a)+int(b)))
    return int(calculate(line))


print(sum([calculate2(x) for x in lines]))
