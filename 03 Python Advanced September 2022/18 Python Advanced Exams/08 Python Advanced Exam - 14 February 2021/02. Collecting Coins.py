size = int(input())
path = []
matrix = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
coins = 0
for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'P' in line:
        current_row = row
        current_col = line.index('P')
        path.append([current_row, current_col])

matrix[path[0][0]][path[0][1]] = '0'
while True:
    direction = input()
    current_row, current_col = path[-1][0] + directions[direction][0], path[-1][1] + directions[direction][1]
    if current_row < 0:
        current_row = size - 1
    elif current_row >= size:
        current_row = 0
    if current_col < 0:
        current_col = size - 1
    elif current_col >= size:
        current_col = 0
    if matrix[current_row][current_col] == 'X':
        coins = coins // 2
        print(f"Game over! You've collected {coins} coins.")
        path.append([current_row, current_col])
        break
    else:
        coins += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = '0'
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            path.append([current_row, current_col])
            break
    path.append([current_row, current_col])

print("Your path:")
for row in path:
    print(row)
