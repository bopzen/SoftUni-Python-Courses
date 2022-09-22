size = int(input())
matrix = [[int(x) for x in input().split()] for row in range(size)]

coordinates = input().split()
count_alive = 0
total_sum = 0

for coordinate in coordinates:
    row, col = tuple(map(int, coordinate.split(",")))
    bomb = matrix[row][col]
    if bomb > 0:
        start_row = max(row-1, 0)
        start_col = max(col-1, 0)
        end_row = min(row+1, size-1)
        end_col = min(col+1, size-1)
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if matrix[i][j] > 0:
                    matrix[i][j] -= bomb

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            count_alive += 1
            total_sum += matrix[row][col]

print(f"Alive cells: {count_alive}")
print(f"Sum: {total_sum}")
for row in range(size):
    print(' '.join(str(x) for x in matrix[row]))
