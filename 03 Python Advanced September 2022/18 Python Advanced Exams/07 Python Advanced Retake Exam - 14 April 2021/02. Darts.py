size = 7
players = input().split(", ")
score_players = {
    players[0]: {'score': 501, 'turns': 0},
    players[1]: {'score': 501, 'turns': 0}
}

matrix = [input().split() for row in range(size)]

while True:
    current_player = players[0]
    score_players[current_player]['turns'] += 1
    coordinates = input()[1:-1].split(", ")
    row, col = int(coordinates[0]), int(coordinates[1])
    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'B':
            break
        elif matrix[row][col] == 'D':
            points = int(matrix[row][0]) + int(matrix[row][size-1]) + int(matrix[0][col]) + int(matrix[size-1][col])
            points *= 2
            score_players[current_player]['score'] -= points
            if score_players[current_player]['score'] <= 0:
                break
        elif matrix[row][col] == 'T':
            points = int(matrix[row][0]) + int(matrix[row][size-1]) + int(matrix[0][col]) + int(matrix[size-1][col])
            points *= 3
            score_players[current_player]['score'] -= points
            if score_players[current_player]['score'] <= 0:
                break
        else:
            points = int(matrix[row][col])
            score_players[current_player]['score'] -= points
            if score_players[current_player]['score'] <= 0:
                break
    players[0], players[1] = players[1], players[0]

print(f"{current_player} won the game with {score_players[current_player]['turns']} throws!")