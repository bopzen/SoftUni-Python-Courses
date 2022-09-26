SIZE = 5
matrix = [input().split() for row in range(SIZE)]
shot_targets = []
count_commands = int(input())
current_row = 0
current_col = 0
targets = 0

for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == 'A':
            current_row, current_col = row, col
        if matrix[row][col] == 'x':
            targets += 1


for _ in range(count_commands):
    command = input().split()
    if command[0] == 'move':
        direction = command[1]
        steps = int(command[2])
        start_row, start_col = current_row, current_row
        if direction == 'up':
            if current_row-steps >= 0 and matrix[current_row-steps][current_col] == '.':
                current_row -= steps
        elif direction == 'down':
            if current_row+steps <= SIZE - 1 and matrix[current_row+steps][current_col] == '.':
                current_row += steps
        elif direction == 'left':
            if current_col-steps >= 0 and matrix[current_row][current_col-steps] == '.':
                current_col -= steps
        elif direction == 'right':
            if current_col+steps <= SIZE - 1 and matrix[current_row][current_col+steps] == '.':
                current_col += steps
    elif command[0] == 'shoot':
        direction = command[1]
        bullet_row, bullet_col = current_row, current_col
        while True:
            if direction == 'up':
                if bullet_row == 0:
                    break
                bullet_row -= 1
            elif direction == 'down':
                if bullet_row == SIZE - 1:
                    break
                bullet_row += 1
            elif direction == 'left':
                if bullet_col == 0:
                    break
                bullet_col -= 1
            elif direction == 'right':
                if bullet_col == SIZE - 1:
                    break
                bullet_col += 1
            if matrix[bullet_row][bullet_col] == 'x':
                matrix[bullet_row][bullet_col] = '.'
                shot_targets.append([bullet_row, bullet_col])
                targets -= 1
                break
    if targets == 0:
        break
if targets == 0:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
if shot_targets:
    for row in shot_targets:
        print(row)

