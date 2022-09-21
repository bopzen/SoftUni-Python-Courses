rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

max_total = 0
max_sub_matrix = []

for row in range(rows-1):
    for col in range(cols-1):
        total = 0
        sub_matrix = []
        sub_matrix.append([matrix[row][col], matrix[row][col+1]])
        sub_matrix.append([matrix[row+1][col], matrix[row+1][col + 1]])
        total += sum(sub_matrix[0]) + sum(sub_matrix[1])
        if total > max_total:
            max_total = total
            max_sub_matrix = sub_matrix

for row in range(len(max_sub_matrix)):
    print(" ".join([str(x) for x in max_sub_matrix[row]]))
print(max_total)