def read(fn):
    with open(f'input/{fn}','r') as f:
        return [x.strip() for x in f.readlines()]
def read_test(fn):
    with open(f'input/{fn}.test','r') as f:
        return [x.strip() for x in f.readlines()]

E = enumerate
