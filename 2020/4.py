import pandas as pd
from handy import read

lines = read(4)
"""lines = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        "",
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
        ]
"""
data = [dict()]
for line in lines:
    if line == "":
        data.append(dict())
    else:
        kvpairs = (x.split(':') for x in line.split())
        data[-1].update({k:v for k,v in kvpairs})

df = pd.DataFrame(data)
cols = list(df.columns)
cols.remove('cid')
df = df.dropna(subset=cols)

print(df.shape)

def valid_height(x):
    if x[-2:] == 'cm':
        return 150 <= int(x[:-2]) <= 193
    elif x[-2:] == 'in':
        return 59 <= int(x[:-2]) <= 76
    else:
        return False
def valid_hcl(x):
    if x[0] != '#':
        return False
    allow = set("0123456789abcdef")
    return len(set(x[1:]) - allow) == 0
def valid_pid(x):
    allow = set('0123456789')
    return len(x) == 9 and len(set(x) - allow) == 0
    
validation_criteria = (
       (1920 <= df.byr.astype(int))
        & (df.byr.astype(int) <= 2002)
        & (2010 <= df.iyr.astype(int))
        & (df.iyr.astype(int) <= 2020)
        & (2020 <= df.eyr.astype(int))
        & (df.eyr.astype(int) <= 2030)
        & (df.hgt.map(valid_height))
        & (df.hcl.map(valid_hcl))
        & (df.ecl.isin(('amb','blu','brn','gry','grn','hzl','oth')))
        & (df.pid.map(valid_pid))
   ) 
