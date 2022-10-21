size = 6
matrix = [input().split() for row in range(size)]
points = 0
for _ in range(3):
    coordinates = list(map(int, input()[1:-1].split(", ")))
    row, col = coordinates[0], coordinates[1]
    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'B':
            matrix[row][col] = '0'
            for row in range(size):
                if matrix[row][col].isdigit():
                    points += int(matrix[row][col])

if 100 <= points <= 199:
    prize = 'Football'
    print(f"Good job! You scored {points} points, and you've won {prize}.")
elif 200 <= points <= 299:
    prize = 'Teddy Bear'
    print(f"Good job! You scored {points} points, and you've won {prize}.")
elif points >= 300:
    prize = 'Lego Construction Set'
    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100-points} points more to win a prize.")
