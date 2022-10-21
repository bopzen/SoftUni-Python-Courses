def check_bombs(curr_row, curr_col):
    result = 0
    start_row = curr_row - 1
    start_col = curr_col - 1
    for current_row in range(start_row, start_row+3):
        for current_col in range(start_col, start_col+3):
            if current_row < 0 or current_row >= size or current_col < 0 or current_col >= size:
                continue
            if matrix[current_row][current_col] == '*':
                result += 1
    return str(result)


size = int(input())
count_bombs = int(input())
matrix = []
for row in range(size):
    line = []
    for col in range(size):
        line.append('0')
    matrix.append(line)

for _ in range(count_bombs):
    row_bomb, col_bomb = list(map(int, input()[1:-1].split(", ")))
    matrix[row_bomb][col_bomb] = '*'

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] != '*':
            matrix[row][col] = check_bombs(row, col)

[print(*row) for row in matrix]