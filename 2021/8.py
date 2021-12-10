from handy import read

lines = read(8)

"""lines = [
"be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
"edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
"fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
"fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
"aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
"fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
"dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
"bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
"egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
"gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
        ]"""

def process_line(ln):
    key = [set()]*10
    inputs, output = ln.split('|')

    inputs_by_length = {
       i: 
           [set(x) for x in inputs.split() if len(x) == i] 
           for i in range(8)
         }

    key[1] = inputs_by_length[2][0]
    key[7] = inputs_by_length[3][0]
    key[4] = inputs_by_length[4][0]
    key[8] = inputs_by_length[7][0]
    for w in inputs_by_length[6]:
        if key[4].issubset(w):
            key[9] = w
        elif key[1].issubset(w):
            key[0] = w
        else:
            key[6] = w
    for w in inputs_by_length[5]:
        if key[1].issubset(w):
            key[3] = w
        elif w.issubset(key[9]):
            key[5] = w
        else:
            key[2] = w
    digits = [key.index(set(str(x))) for x in output.split()]
    return int("".join(str(x) for x in digits))

print(sum(process_line(ln) for ln in lines))
