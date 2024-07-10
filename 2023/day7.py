import time
from cmn import loadfile, preproc
import math
import pandas as pd
import numpy as np
data = loadfile('day7.txt', 'https://adventofcode.com/2023/day/7/input')
handmap = {k:v for k, v in zip('AKQJT98765432', 'abcdefghijklm')}

sample = '''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''
# data = preproc(sample)

def rank_hand(hand, wild_jacks=False):
    if (not isinstance(hand, str)) or len(hand) != 5:
        raise Exception("Bad hand:", hand)
    hand = pd.Series(list(hand))
    if wild_jacks and 'J' in list(hand):
        top_hand_showings = [c for c in hand.value_counts().sort_values(ascending=False).index if c != 'J']
        if len(top_hand_showings) == 0:
            return 6
        else:
            hand = hand.replace('J', top_hand_showings[0])
    if hand.value_counts().max() == 5:
        return 6
    if hand.value_counts().max() == 4:
        return 5
    if hand.value_counts().max() == 3:
        if hand.value_counts().min() == 2:
            return 4
        else:
            return 3
    if hand.value_counts().max() == 2:
        if hand.value_counts().median() == 2:
            return 2
        else:
            return 1
    else: 
        return 0
def rejigger(hand, handmap=handmap):
    ret = hand
    for k,v in handmap.items():
        ret = ret.replace(k,v)
    return ret

results = [(rank_hand(hand), rejigger(hand) , bid) for hand, bid in [r.split() for r in data]]
results = sorted(results, key=lambda x: x[1], reverse=False)
results = sorted(results, key=lambda x: x[0], reverse=True)
df = pd.DataFrame(results, columns=['hand_rank','hand','bid'])
N = len(df)
df['ix'] = N - df.index.to_series()
print((df.ix * df.bid.astype(int)).sum())


new_handmap = {k:v for k, v in zip('AKQT98765432J', 'abcdefghijklm')}
results = [(rank_hand(hand, wild_jacks=True), rejigger(hand, new_handmap) , bid) for hand, bid in [r.split() for r in data]]
results = sorted(results, key=lambda x: x[1], reverse=False)
results = sorted(results, key=lambda x: x[0], reverse=True)
df = pd.DataFrame(results, columns=['hand_rank','hand','bid'])
N = len(df)
df['ix'] = N - df.index.to_series()
print((df.ix * df.bid.astype(int)).sum())