rows, columns = list(map(int, input().split(", ")))

matrix = []
for row in range(rows):
    line = list(map(int, input().split(" ")))
    matrix.append(line)

for column in range(columns):
    sum_column = 0
    for row in range(rows):
        sum_column += matrix[row][column]
    print(sum_column)