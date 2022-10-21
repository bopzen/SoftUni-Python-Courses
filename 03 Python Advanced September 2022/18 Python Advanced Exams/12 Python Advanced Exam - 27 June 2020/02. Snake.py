size = int(input())
current_row = 0
current_col = 0
out_of_matrix = False
food = 0
burrows = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix = []
for row in range(size):
    line = list(input())
    matrix.append(line)
    if 'S' in line:
        current_row = row
        current_col = line.index('S')
    if 'B' in line:
        burrow = [row, line.index('B')]
        burrows.append(burrow)

while True:
    command = input()
    matrix[current_row][current_col] = '.'
    current_row += directions[command][0]
    current_col += directions[command][1]
    if current_row < 0 or current_row >= size or current_col < 0 or current_col >= size:
        out_of_matrix = True
        print('Game over!')
        break
    if matrix[current_row][current_col] == '*':
        food += 1
        matrix[current_row][current_col] = 'S'
        if food == 10:
            break
    elif matrix[current_row][current_col] == 'B':
        burrows.remove([current_row, current_col])
        matrix[current_row][current_col] = '.'
        current_row, current_col = burrows[0][0], burrows[0][1]
        matrix[current_row][current_col] = 'S'

if food == 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")

[print(''.join(row)) for row in matrix]