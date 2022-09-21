rows, cols = [int(x) for x in input().split()]

matrix = [input().split(" ") for row in range(rows)]
counter = 0
for row in range(rows-1):
    for col in range(cols-1):
        is_equal = True
        sub_matrix = [[matrix[x][y] for y in range(col, col+2)] for x in range(row, row+2)]
        for i in range(len(sub_matrix)):
            for j in range(len(sub_matrix)):
                if sub_matrix[i][j] != matrix[row][col]:
                    is_equal = False
                    break
            if not is_equal:
                break
        if is_equal:
            counter +=1
print(counter)