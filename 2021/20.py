from handy import *

lines = read(20)
#lines = read_test(20)

alg = lines[0]
img = lines[2:]

img_h = len(img)
img_w = len(img[0])

def expand_img(char="."):
    global img
    global img_h, img_w
    img = [char+x+char for x in img]
    img_w += 2
    img = [char*img_w]+img+[char*img_w]
    img_h += 2

def pmap(img, r, c):
    s = img[r-1][c-1:c+2]+img[r][c-1:c+2]+img[r+1][c-1:c+2]
    return alg[int(s.replace('.','0').replace('#','1'), base=2)]

flip = True
print('\n'.join(img))
def enhance():
    global img, img_h, img_w,flip
    expand_img('.' if flip else '#')
    expand_img('.' if flip else '#')
    expand_img('.' if flip else '#')
    flip = not flip
    img_copy = [list(x) for x in img]
    out = []
    for r in range(1, img_h-1):
        for c in range(1, img_w-1):
            img_copy[r][c] = pmap(img, r, c)
#    print("\n".join(["".join(z) for z in img_copy]))
    img = ["".join(z[1:-1]) for z in img_copy[1:-1]]
    img_w -= 2
    img_h -= 2
    print("\n".join(img))
            
