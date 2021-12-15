
lines = read_test(12)
lines = read(12)

lines = [(x[0], int(x[1:])) for x in lines]


def turn(facing, deg):
    new = facing + deg
    while new >= 360:
        new = new - 360
    while new < 0:
        new = new + 360
    return new


def execute(cmd,n):
    global x, y, facing
    if cmd == 'N':
        y += n
    elif cmd == 'S':
        y -= n
    elif cmd == 'E':
        x += n
    elif cmd == 'W':
        x -= n
    elif cmd == 'R':
        facing = turn(facing, n)
    elif cmd == 'L':
        facing = turn(facing, -n)
    elif cmd == 'F':
        if facing == 0:
            y += n
        elif facing == 90:
            x += n
        elif facing == 180:
            y -= n
        elif facing == 270:
            x -= n
        else: raise Exception(facing)
    else:
        raise Exception()

def rotate(x, y, deg):
    if deg in (0, 360):
        return x,y
    elif deg in (90, -270):
        return y, -x
    elif abs(deg) == 180:
        return -x, -y
    elif deg in (270, -90):
        return -y, x
def execute2(cmd,n):
    global x, y, facing,wx,wy
    if cmd == 'N': wy += n
    elif cmd == 'S': wy -= n
    elif cmd == 'E': wx += n
    elif cmd == 'W': wx -= n
    elif cmd == 'R':
        wx, wy = rotate(wx, wy, n)
    elif cmd == 'L':
        wx, wy = rotate(wx, wy, -n)
    elif cmd == 'F':
        for i in range(n): x, y = x + wx, y + wy
    else:
        raise Exception()
facing = 90
x, y = 0, 0
wx, wy = 10, 1

print(f'x={x} y={y} facing={facing}')

for cmd, n in lines:
    execute2(cmd,n)
#    print(cmd,n)
#    print(f'x={x} y={y} facing={facing}')

print(abs(x)+abs(y))



