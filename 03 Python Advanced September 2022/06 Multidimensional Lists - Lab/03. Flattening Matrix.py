rows = int(input())
matrix = []

for row in range(rows):
    line = list(map(int, input().split(", ")))
    matrix.append(line)

flattened_matrix = [x for row in matrix for x in row]
print(flattened_matrix)