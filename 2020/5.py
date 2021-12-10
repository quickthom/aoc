from handy import read

lines = read(5)

def get_coords(line):
    row = int(line[:7].replace('F','0').replace('B','1'), base=2)
    col = int(line[7:].replace('L','0').replace('R','1'), base=2)
    seat_id = row * 8 + col
    return row, col, seat_id

seat_ids = [x[2] for x in map(get_coords, lines)]
print(max(seat_ids))

myseat_idx = np.argmax(np.diff(sorted(seat_ids)))
print('Seat ID:',sorted(seat_ids)[myseat_idx] + 1)
