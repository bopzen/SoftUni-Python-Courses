size = int(input())
matrix = [list(input()) for row in range(size)]
max_count_attacks = 0
count_removed_knights = 0
while True:
    count_attacks = 0
    max_count_attacks = 0
    max_attack_row = 0
    max_attack_col = 0
    for row in range(size):
        for col in range(size):
            count_knight_attacks = 0
            if matrix[row][col] == "K":
                if row-1 >= 0 and col-2 >= 0:
                    if matrix[row-1][col-2] == 'K':
                        count_knight_attacks += 1
                if row-2 >= 0 and col-1 >= 0:
                    if matrix[row-2][col-1] == 'K':
                        count_knight_attacks += 1
                if row-2 >= 0 and col+1 <= size-1:
                    if matrix[row-2][col+1] == 'K':
                        count_knight_attacks += 1
                if row-1 >= 0 and col+2 <= size-1:
                    if matrix[row-1][col+2] == 'K':
                        count_knight_attacks += 1
                if row+1 <= size-1 and col+2 <= size-1:
                    if matrix[row+1][col+2] == 'K':
                        count_knight_attacks += 1
                if row+2 <= size-1 and col+1 <= size-1:
                    if matrix[row+2][col+1] == 'K':
                        count_knight_attacks += 1
                if row+2 <= size-1 and col-1 >= 0:
                    if matrix[row+2][col-1] == 'K':
                        count_knight_attacks += 1
                if row+1 <= size-1 and col-2 >= 0:
                    if matrix[row+1][col-2] == 'K':
                        count_knight_attacks += 1
            if count_knight_attacks > max_count_attacks:
                max_count_attacks = count_knight_attacks
                max_attack_row = row
                max_attack_col = col
    if max_count_attacks > 0:
        matrix[max_attack_row][max_attack_col] = '0'
        count_removed_knights += 1
    else:
        break
print(count_removed_knights)