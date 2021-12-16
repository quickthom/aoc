from handy import *

lines = read(14)
#lines = read_test(14)

def extract_mask(line):
    mask = line.split(' = ')[1]
    or_mask = int(mask.replace('X', '0'), base=2)
    and_mask = int(mask.replace('X', '1'), base=2)
    return and_mask, or_mask

def extract_memop(line):
    close_bracket = line.find(']')
    address = int(line[4:close_bracket])
    return address, int(line.split('= ')[1])

mem = dict()
for line in lines:
    if line[:2] == 'ma':
        and_mask, or_mask = extract_mask(line)
    else:
        address, value = extract_memop(line)
        mem[address] = value & and_mask | or_mask
print(sum(mem.values()))

def extract_masks(line):
    mask = line.split(' = ')[1]
    or_mask = int(mask.replace('X', '0'), base=2)
    xors = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            xors.append(2**(len(mask)-i-1))
    return or_mask, xors

mem = dict()
for line in lines:
    if line[:2] == 'ma':
        or_mask, xors = extract_masks(line)
    else:
        address, value = extract_memop(line)
        a = address | or_mask
        mem[a] = value
        for how in range(1,len(xors)+1):
            for combo in combinations(xors, how):
                mem[a ^ sum(combo)] = value

print(sum(mem.values()))
