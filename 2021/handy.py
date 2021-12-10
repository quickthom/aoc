def read(fn):
    with open(f'input/{fn}','r') as f:
        return [x.strip() for x in f.readlines()]
