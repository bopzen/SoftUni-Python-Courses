
text = input()
size = int(input())
current_row = 0
current_col = 0
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
    if 'P' in line:
        current_row = row
        current_col = line.index('P')

m = int(input())

for _ in range(m):
    command = input()
    matrix[current_row][current_col] = '-'
    if current_row + directions[command][0] < 0 or current_row + directions[command][0] >= size or current_col + directions[command][1] < 0 or current_col + directions[command][1] >= size:
        if len(text) > 0:
            text = text[:-1]
    else:
        current_row += directions[command][0]
        current_col += directions[command][1]
        if matrix[current_row][current_col] != '-':
            text += matrix[current_row][current_col]
    matrix[current_row][current_col] = 'P'
print(text)
for row in matrix:
    print("".join(row))