def check_matrix():
    for line in matrix:
        if 'D' in line or 'G' in line or 'C' in line:
            return False
    return True


rows, cols = tuple(map(int,input().split(", ")))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

collected_items = {
    'Christmas decorations' : 0,
    'Gifts': 0,
    'Cookies': 0
}

current_row = 0
current_col = 0

matrix = []
for row in range(rows):
    line = input().split()
    matrix.append(line)
    if 'Y' in line:
        current_row = row
        current_col = line.index('Y')

while True:
    command = input()
    if command == 'End':
        break
    command_elements = command.split('-')
    direction, steps = command_elements[0], int(command_elements[1])
    for step in range(steps):
        if check_matrix():
            break
        matrix[current_row][current_col] = 'x'
        current_row += directions[direction][0]
        if current_row < 0:
            current_row = rows - 1
        elif current_row > rows - 1:
            current_row = 0
        current_col += directions[direction][1]
        if current_col < 0:
            current_col = cols - 1
        elif current_col > cols -1:
            current_col = 0
        if matrix[current_row][current_col] == 'D':
            collected_items['Christmas decorations'] += 1
        elif matrix[current_row][current_col] == 'G':
            collected_items['Gifts'] += 1
        elif matrix[current_row][current_col] == 'C':
            collected_items['Cookies'] += 1
        matrix[current_row][current_col] = 'Y'
    if check_matrix():
        print("Merry Christmas!")
        break

print("You've collected:")
for key, value in collected_items.items():
    print(f"- {value} {key}")

[print(*row) for row in matrix]
