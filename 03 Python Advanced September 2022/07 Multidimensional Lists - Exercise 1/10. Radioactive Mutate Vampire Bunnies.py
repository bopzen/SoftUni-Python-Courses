rows, cols = [int(x) for x in input().split()]
lair = [list(input()) for row in range(rows)]
directions = list(input())
current_row = 0
current_col = 0
has_escaped = False
is_dead = False
bunnies = []

for row in range(rows):
    for col in range(cols):
        if lair[row][col] == 'P':
            current_row = row
            current_col = col
        elif lair[row][col] == 'B':
            bunnies.append([row, col])
            
lair[current_row][current_col] = '.'

for direction in directions:
    if direction == 'R':
        if current_col == cols - 1:
            has_escaped = True
            lair[current_row][current_col] = '.'
        else:
            current_col += 1
    elif direction == 'L':
        if current_col == 0:
            has_escaped = True
            lair[current_row][current_col] = '.'
        else:
            current_col -= 1
    elif direction == 'U':
        if current_row == 0:
            has_escaped = True
            lair[current_row][current_col] = '.'
        else:
            current_row -= 1
    elif direction == 'D':
        if current_row == rows - 1:
            has_escaped = True
            lair[current_row][current_col] = '.'
        else:
            current_row += 1
    for coordinates in bunnies:
        row, col = coordinates[0], coordinates[1]
        if lair[row][col] == 'B':
            lair[max(row-1, 0)][col] = 'B'
            lair[min(row + 1, rows - 1)][col] = 'B'
            lair[row][max(col - 1, 0)] = 'B'
            lair[row][min(col + 1, cols - 1)] = 'B'
    for row in range(rows):
        for col in range(cols):
            if lair[row][col] == 'B' and [row,col] not in bunnies:
                bunnies.append([row, col])
    if has_escaped:
        break
    if lair[current_row][current_col] == 'B':
        is_dead = True
        break

for row in range(rows):
    print(''.join(lair[row]))
if has_escaped:
    print(f"won: {current_row} {current_col}")
if is_dead:
    print(f"dead: {current_row} {current_col}")