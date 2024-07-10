import requests
import os

cookie = {
    'session':'53616c7465645f5f0dd6697f2a8fada40e904fd407fa090c6dd5c2c5c714b5d6bf83ed0b32ce816a06c146d380a41d7a306cb17275cb3ac94a914d902ef52690'
}
def loadfile(f, url):
    if not os.path.isfile(f):
        response = requests.get(url,cookies=cookie)
        print(response)
        if response.status_code == 200:
            with open(f, 'wb') as file:
                file.write(response.content)
    with open(f,'r') as file:
        return [line.strip() for line in file.readlines()]

vals = loadfile('day1.txt', 'https://adventofcode.com/2023/day/1/input')
som = 0
for v in vals:
    calibration_value = [None, None]
    for c in v:
        if c.isnumeric():
            if calibration_value[0] is None:
                calibration_value[0] = c
            calibration_value[1] = c   
    som += int(''.join(calibration_value))

print(som)

adjust_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}

def first_number(word):
    first = 'na'
    low = 99
    ltr = None
    for k, v in adjust_map.items():
        try:
            z = word.index(k)
            if z < low:
                first = v
                low = z
                ltr = k
        except ValueError:
            pass                
        try:
            z = word.index(v)
            if z < low:
                first = v
                low = z
                ltr = None
        except ValueError:
            pass
    return first, ltr

def last_number(word):
    last = 'na'
    hi = -1
    for k, v in adjust_map.items():
        for n in range(len(word)):
            subword = word[n:]
            try:
                z = subword.index(k)
                if z + n > hi:
                    last = v
                    hi = z + n
            except ValueError:
                pass                
            try:
                z = subword.index(v)
                if z + n > hi:
                    last = v
                    hi = z + n
            except ValueError:
                pass
    return last    
vals = loadfile('day1.txt', 'https://adventofcode.com/2023/day/1/input')

# vals = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen",
#     "eighthree",
#     "sevenine"
# ]
# correct = 443

som = 0
calibs = []
for v in vals:
    first, ltr = first_number(v)
    if ltr is not None:
        v = v.replace(ltr, adjust_map[ltr], 0)
    last = last_number(v)
    calibration_value = int(''.join([first,last]))
    print(calibration_value)
    calibs.append(calibration_value)
    som += calibration_value

print(som)

som = 0
calibs2 = []
for line in vals:
        digits = []
        # start at the first letter and move through it letter by letter.
        # this is the only way i've found to account for overlapping words.
        # an example is "oneight", which only matches "one" when using re.findall.
        for i,c in enumerate(line):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                for k in adjust_map.keys():
                    if line[i:].startswith(k):
                        digits.append(adjust_map[k])
        calibs2.append(int(f"{digits[0]}{digits[-1]}"))
    
print(sum(calibs2))
