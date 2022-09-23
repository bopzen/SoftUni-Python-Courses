size = int(input())
matrix = [input().split() for row in range(size)]

current_row = 0
current_col = 0
tea_bags = 0
is_alice_found = False
has_ended = False
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'A':
            current_row, current_col = row, col
            is_alice_found = True
            break
    if is_alice_found:
        break
matrix[current_row][current_col] = '*'
while True:
    command = input()
    if command == 'up':
        current_row -= 1
        if current_row < 0:
            has_ended = True
            break
        elif matrix[current_row][current_col] == 'R':
            matrix[current_row][current_col] = '*'
            has_ended = True
            break
    elif command == 'down':
        current_row += 1
        if current_row >= size:
            has_ended = True
            break
        elif matrix[current_row][current_col] == 'R':
            matrix[current_row][current_col] = '*'
            has_ended = True
            break
    elif command == 'left':
        current_col -= 1
        if current_col < 0:
            has_ended = True
            break
        elif matrix[current_row][current_col] == 'R':
            matrix[current_row][current_col] = '*'
            has_ended = True
            break
    elif command == 'right':
        current_col += 1
        if current_col >= size:
            has_ended = True
            break
        elif matrix[current_row][current_col] == 'R':
            matrix[current_row][current_col] = '*'
            has_ended = True
            break
    if matrix[current_row][current_col].isdigit():
        tea_bags += int(matrix[current_row][current_col])
    matrix[current_row][current_col] = '*'
    if tea_bags >= 10:
        break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]