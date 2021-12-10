from handy import read

lines = read(8)
#lines = [ "nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3", "acc -99", "acc +1", "jmp -4", "acc +6", ]

def execute(lines):
    pgmc = 0
    pgmc_hist = set()
    acc = 0
    while pgmc < len(lines) and pgmc not in pgmc_hist:
        pgmc_hist.add(pgmc)
        cmd, arg = lines[pgmc].split()
        if cmd =='acc':
            acc += int(arg)
        pgmc += int(arg) if cmd=='jmp' else 1
    if pgmc != len(lines):
        return False, acc
    return True, acc
execute(lines)

nops_and_jmps = [i for i, cmd in enumerate(lines) if cmd[:3] in ('nop','jmp')]

for i in nops_and_jmps:
    new = lines.copy()
    repl=('nop','jmp') if 'nop' in new[i] else ('jmp','nop')
    new[i] = new[i].replace(*repl)
    clean, acc = execute(new)
    if clean:
        break
print(acc)
