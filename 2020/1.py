from handy import read

lines = list(map(int,read(1)))

for i,a in enumerate(lines):
    for j,b in enumerate(lines[i+1:]):
        for c in lines[i+j+1:]:
            if a+b+c == 2020:
                print(a,b,c,a+b+c,a*b*c)

