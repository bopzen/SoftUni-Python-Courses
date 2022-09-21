rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        palindrome = chr(97+row) + chr(97+row+col) + chr(97+row)
        matrix[row].append(palindrome)

for row in range(rows):
    print(' '.join(x for x in matrix[row]))






