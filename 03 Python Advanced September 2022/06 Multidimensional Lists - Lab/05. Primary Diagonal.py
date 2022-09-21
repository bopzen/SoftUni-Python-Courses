rows = int(input())
matrix = []
for row in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)
total = 0
for i in range(rows):
    total += matrix[i][i]

print(total)