presents = int(input())
size = int(input())
nice_kids = 0
nice_kids_reached = 0
current_row, current_col = 0, 0
matrix = []
for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'S' in line:
        current_row, current_col = row, line.index('S')
    if 'V' in line:
        nice_kids += line.count('V')

while True:
    command = input()
    if command == 'Christmas morning':
        break
    if command == 'up':
        if current_row - 1 < 0:
            continue
        else:
            matrix[current_row][current_col] = '-'
            current_row -= 1
            if matrix[current_row][current_col] == 'X':
                matrix[current_row][current_col] = 'S'
                continue
            elif matrix[current_row][current_col] == 'V':
                presents -= 1
                nice_kids -= 1
                nice_kids_reached += 1
                matrix[current_row][current_col] = 'S'
            elif matrix[current_row][current_col] == 'C':
                matrix[current_row][current_col] = 'S'
                if matrix[current_row-1][current_col] != '-':
                    presents -= 1
                    if matrix[current_row-1][current_col] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row-1][current_col] = '-'
                if matrix[current_row+1][current_col] != '-':
                    presents -= 1
                    if matrix[current_row+1][current_col] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row+1][current_col] = '-'
                if matrix[current_row][current_col-1] != '-':
                    presents -= 1
                    if matrix[current_row][current_col-1] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row][current_col-1] = '-'
                if matrix[current_row][current_col+1] != '-':
                    presents -= 1
                    if matrix[current_row][current_col+1] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row][current_col+1] = '-'
    elif command == 'down':
        if current_row + 1 >= size:
            continue
        else:
            matrix[current_row][current_col] = '-'
            current_row += 1
            if matrix[current_row][current_col] == 'X':
                matrix[current_row][current_col] = 'S'
                continue
            elif matrix[current_row][current_col] == 'V':
                presents -= 1
                nice_kids -= 1
                nice_kids_reached += 1
                matrix[current_row][current_col] = 'S'
            elif matrix[current_row][current_col] == 'C':
                matrix[current_row][current_col] = 'S'
                if matrix[current_row-1][current_col] != '-':
                    presents -= 1
                    if matrix[current_row-1][current_col] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row-1][current_col] = '-'
                if matrix[current_row+1][current_col] != '-':
                    presents -= 1
                    if matrix[current_row+1][current_col] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row+1][current_col] = '-'
                if matrix[current_row][current_col-1] != '-':
                    presents -= 1
                    if matrix[current_row][current_col-1] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row][current_col-1] = '-'
                if matrix[current_row][current_col+1] != '-':
                    presents -= 1
                    if matrix[current_row][current_col+1] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row][current_col+1] = '-'
    elif command == 'left':
        if current_col - 1 < 0:
            continue
        else:
            matrix[current_row][current_col] = '-'
            current_col -= 1
            if matrix[current_row][current_col] == 'X':
                matrix[current_row][current_col] = 'S'
                continue
            elif matrix[current_row][current_col] == 'V':
                presents -= 1
                nice_kids -= 1
                nice_kids_reached += 1
                matrix[current_row][current_col] = 'S'
            elif matrix[current_row][current_col] == 'C':
                matrix[current_row][current_col] = 'S'
                if matrix[current_row-1][current_col] != '-':
                    presents -= 1
                    if matrix[current_row-1][current_col] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row-1][current_col] = '-'
                if matrix[current_row+1][current_col] != '-':
                    presents -= 1
                    if matrix[current_row+1][current_col] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row+1][current_col] = '-'
                if matrix[current_row][current_col-1] != '-':
                    presents -= 1
                    if matrix[current_row][current_col-1] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row][current_col-1] = '-'
                if matrix[current_row][current_col+1] != '-':
                    presents -= 1
                    if matrix[current_row][current_col+1] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row][current_col+1] = '-'
    elif command == 'right':
        if current_col + 1 >= size:
            continue
        else:
            matrix[current_row][current_col] = '-'
            current_col += 1
            if matrix[current_row][current_col] == 'X':
                matrix[current_row][current_col] = 'S'
                continue
            elif matrix[current_row][current_col] == 'V':
                presents -= 1
                nice_kids -= 1
                nice_kids_reached += 1
                matrix[current_row][current_col] = 'S'
            elif matrix[current_row][current_col] == 'C':
                matrix[current_row][current_col] = 'S'
                if matrix[current_row-1][current_col] != '-':
                    presents -= 1
                    if matrix[current_row-1][current_col] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row-1][current_col] = '-'
                if matrix[current_row+1][current_col] != '-':
                    presents -= 1
                    if matrix[current_row+1][current_col] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row+1][current_col] = '-'
                if matrix[current_row][current_col-1] != '-':
                    presents -= 1
                    if matrix[current_row][current_col-1] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row][current_col-1] = '-'
                if matrix[current_row][current_col+1] != '-':
                    presents -= 1
                    if matrix[current_row][current_col+1] == 'V':
                        nice_kids -= 1
                        nice_kids_reached += 1
                    matrix[current_row][current_col+1] = '-'
    if presents == 0:
        break

if nice_kids > 0 and presents == 0:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_reached} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")