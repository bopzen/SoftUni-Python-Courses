size = int(input())
matrix = [[int(x) for x in input().split()] for rows in range(size)]

while True:
    command = input()
    if command == 'END':
        break
    action, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if action == 'Add' and 0 <= row <= size -1 and 0 <= col <= size -1:
        matrix[row][col] += value
    elif action == 'Subtract' and 0 <= row <= size -1 and 0 <= col <= size -1:
        matrix[row][col] -= value
    else:
        print('Invalid coordinates')

[print(*matrix[row]) for row in range(size)]