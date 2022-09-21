size = int(input())
matrix = []
for row in range(size):
    line = list(input())
    matrix.append(line)
symbol = input()
is_found = False
for row in range(size):
    for col in range(size):
        if matrix[row][col] == symbol:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f"({row}, {col})")
else:
    print(f"{symbol} does not occur in the matrix")