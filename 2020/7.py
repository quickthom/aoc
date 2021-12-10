from handy import read

lines = read(7)
"""lines = [

"light red bags contain 1 bright white bag, 2 muted yellow bags.",
"dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
"bright white bags contain 1 shiny gold bag.",
"muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
"shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
"dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
"vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
"faded blue bags contain no other bags.",
"dotted black bags contain no other bags.",
        ]"""

all_bags = dict()

def break_off_qty(x):
    space = x.index(' ')
    qty = int(x[:space])
    return qty, x[space:].strip()

for line in lines:
    bagtype, contents = line.split(' contain ')
    bagtype = bagtype.replace(' bags','').strip()
    contents = contents.replace(' bags','').replace(' bag','').replace('.','').strip().split(', ')
    if contents[0] == 'no other':
        contents = []
        root_bags.append(bagtype)
    contents = [break_off_qty(x) for x in contents]
    all_bags[bagtype] = contents
    print(bagtype, contents)

def holds_gold(bagtype):
    for holding in all_bags[bagtype]:
        if holding[1] == 'shiny gold' or holds_gold(holding[1]):
            return True
    return False

print(sum([holds_gold(x) for x in all_bags.keys()]))

def required_contents_qty(bagtype):
    if not all_bags[bagtype]:
        return 0
    direct = sum([x[0] for x in all_bags[bagtype]])
    below = sum((required_contents_qty(x[1])*x[0] for x in all_bags[bagtype]))
    return direct + below

    



