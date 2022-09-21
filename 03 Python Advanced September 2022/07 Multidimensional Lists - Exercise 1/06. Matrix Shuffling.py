rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for row in range(rows)]

while True:
    command = input()
    if command == 'END':
        break
    tokens = command.split()
    if tokens[0] == 'swap' and len(tokens) == 5 and 0 <= int(tokens[1]) <= rows and 0 <= int(tokens[2]) <= cols and 0 <= int(tokens[3]) <= rows and 0 <= int(tokens[4]) <= cols:
        row1, col1, row2, col2 = int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4])
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in range(rows):
            print(' '.join(str(x) for x in matrix[row]))

    else:
        print('Invalid input!')




