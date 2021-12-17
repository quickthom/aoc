from handy import *

card_key, door_key = map(int, read(25))
#card_key, door_key = map(int, read_test(25))


def transform(subject, loop):
    v = 1
    for _ in range(1, loop+1):
        v *= subject
        v = v % 20201227
    return v    

def reverse_engineer(public_key):
    v = 1
    for loop in range(1,100000000):
        v *= 7
        v = v % 20201227
        if v == public_key:
            return loop
    raise Exception()

card_loop = reverse_engineer(card_key)
door_loop = reverse_engineer(door_key)

print(transform(door_key, card_loop))
print(transform(card_key, door_loop))
