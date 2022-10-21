size = 8

queens = []
capture_queens = []
king = []
matrix = []
for row in range(size):
    queen = []
    line = input().split()
    matrix.append(line)
    if 'K' in line:
        king.append(row)
        king.append(line.index('K'))
    for i in range(len(line)):
        if line[i] == 'Q':
            queen.append(row)
            queen.append(i)
            queens.append(queen)
        queen = []

row_king, col_king = king[0], king[1]
for queen in queens:
    row_queen, col_queen = queen[0], queen[1]
    if row_king == row_queen:
        distance = col_king - col_queen
        while True:
            col_queen += int(distance/abs(distance))
            if col_queen < 0 or col_queen >= size:
                break
            if matrix[row_queen][col_queen] == 'Q':
                break
            if matrix[row_queen][col_queen] == 'K':
                capture_queens.append(queen)
                break
    elif col_king == col_queen:
        distance = row_king - row_queen
        while True:
            row_queen += int(distance/abs(distance))
            if row_queen < 0 or row_queen >= size:
                break
            if matrix[row_queen][col_queen] == 'Q':
                break
            if matrix[row_queen][col_queen] == 'K':
                capture_queens.append(queen)
                break
    elif abs(row_king - row_queen) == abs(col_king - col_queen):
        distance_row = row_king - row_queen
        distance_col = col_king - col_queen
        while True:
            row_queen += int(distance_row/abs(distance_row))
            col_queen += int(distance_col/abs(distance_col))
            if row_queen < 0 or row_queen >= size or col_queen < 0 or col_queen >= size:
                break
            if matrix[row_queen][col_queen] == 'Q':
                break
            if matrix[row_queen][col_queen] == 'K':
                capture_queens.append(queen)
                break
if capture_queens:
    for queen in capture_queens:
        print(queen)
else:
    print("The king is safe!")