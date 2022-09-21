rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split(" ")] for row in range(rows)]
max_sub_matrix = []
max_total = -100000

for row in range(rows-2):
    for col in range(cols-2):
        sub_matrix = [[matrix[x][y] for y in range(col, col+3)] for x in range(row, row+3)]
        total = 0
        for i in range(len(sub_matrix)):
            for j in range(len(sub_matrix)):
                total += sub_matrix[i][j]
        if total > max_total:
            max_total = total
            max_sub_matrix = sub_matrix
print(f"Sum = {max_total}")
for row in range(len(max_sub_matrix)):
    print(" ".join([str(x) for x in max_sub_matrix[row]]))






