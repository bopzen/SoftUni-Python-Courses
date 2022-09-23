size = int(input())
matrix = [input().split() for row in range(size)]
bunny_row = 0
bunny_col = 0
directions = ['left', 'right', 'up', 'down']
best_direction = ''
best_list_eggs = []
best_sum_eggs = -10000
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny_row = row
            bunny_col = col
for direction in directions:
    list_eggs = []
    sum_eggs = 0
    current_row = bunny_row
    current_col = bunny_col
    if direction == 'left':
        while True:
            current_col -= 1
            if current_col < 0 or matrix[current_row][current_col] == 'X':
                break
            sum_eggs += int(matrix[current_row][current_col])
            list_eggs.append([current_row, current_col])
        if sum_eggs > best_sum_eggs and list_eggs:
            best_direction = direction
            best_sum_eggs = sum_eggs
            best_list_eggs = [row for row in list_eggs]
    elif direction == 'right':
        while True:
            current_col += 1
            if current_col >= size or matrix[current_row][current_col] == 'X':
                break
            sum_eggs += int(matrix[current_row][current_col])
            list_eggs.append([current_row, current_col])
        if sum_eggs > best_sum_eggs and list_eggs:
            best_direction = direction
            best_sum_eggs = sum_eggs
            best_list_eggs = [row for row in list_eggs]
    elif direction == 'up':
        while True:
            current_row -= 1
            if current_row < 0 or matrix[current_row][current_col] == 'X':
                break
            sum_eggs += int(matrix[current_row][current_col])
            list_eggs.append([current_row, current_col])
        if sum_eggs > best_sum_eggs and list_eggs:
            best_direction = direction
            best_sum_eggs = sum_eggs
            best_list_eggs = [row for row in list_eggs]
    elif direction == 'down':
        while True:
            current_row += 1
            if current_row >= size or matrix[current_row][current_col] == 'X':
                break
            sum_eggs += int(matrix[current_row][current_col])
            list_eggs.append([current_row, current_col])
        if sum_eggs > best_sum_eggs and list_eggs:
            best_direction = direction
            best_sum_eggs = sum_eggs
            best_list_eggs = [row for row in list_eggs]
print(best_direction)
[print(row) for row in best_list_eggs]
print(best_sum_eggs)