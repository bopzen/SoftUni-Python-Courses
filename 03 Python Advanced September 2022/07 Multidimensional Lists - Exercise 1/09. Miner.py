size = int(input())
directions = input().split()
matrix = [input().split() for row in range(size)]
collected_coal = 0
total_coal = 0
current_row = 0
current_col = 0
is_collected = False
is_end = False
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 's':
            current_row = row
            current_col = col
        elif matrix[row][col] == 'c':
            total_coal += 1

for direction in directions:
    if direction == 'up':
        if current_row > 0:
            current_row -= 1
        else:
            continue
    elif direction == 'down':
        if current_row < size-1:
            current_row += 1
        else:
            continue
    elif direction == 'left':
        if current_col > 0:
            current_col -= 1
        else:
            continue
    elif direction == 'right':
        if current_col < size-1:
            current_col += 1
        else:
            continue
    if matrix[current_row][current_col] == 'c':
        collected_coal += 1
        matrix[current_row][current_col] = '*'
    if collected_coal == total_coal:
        is_collected = True
        break
    if matrix[current_row][current_col] == 'e':
        is_end = True
        break
else:
    print(f"{total_coal-collected_coal} pieces of coal left. ({current_row}, {current_col})")

if is_collected:
    print(f"You collected all coal! ({current_row}, {current_col})")
if is_end:
    print(f"Game over! ({current_row}, {current_col})")

