size = 6
matrix = [input().split() for row in range(size)]
coordinates = input()[1:-1].split(", ")
current_row, current_col = int(coordinates[0]), int(coordinates[1])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == 'Stop':
        break
    tokens = command.split(", ")
    action, direction = tokens[0], tokens[1]
    current_row += directions[direction][0]
    current_col += directions[direction][1]
    if action == 'Create':
        value = tokens[2]
        if matrix[current_row][current_col] == '.':
            matrix[current_row][current_col] = value
    elif action == 'Update':
        value = tokens[2]
        if matrix[current_row][current_col] != '.':
            matrix[current_row][current_col] = value
    elif action == 'Delete':
        if matrix[current_row][current_col] != '.':
            matrix[current_row][current_col] = '.'
    elif action == 'Read':
        if matrix[current_row][current_col] != '.':
            print(matrix[current_row][current_col])
[print(*row) for row in matrix]