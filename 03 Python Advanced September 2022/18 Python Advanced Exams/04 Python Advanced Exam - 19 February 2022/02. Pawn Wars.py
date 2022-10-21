size = 8

pawn_w_coord = [0, 0]
pawn_b_coord = [0, 0]
pawns = ['w', 'b']

chess_board = []
for row in range(8, 0, -1):
    line = []
    for col in 'abcdefgh':
        line.append(col + str(row))
    chess_board.append(line)

matrix = []
for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'w' in line:
        pawn_w_coord[0] = row
        pawn_w_coord[1] = line.index('w')
    if 'b' in line:
        pawn_b_coord[0] = row
        pawn_b_coord[1] = line.index('b')


while True:
    current_pawn = pawns[0]
    if abs(pawn_w_coord[0]-pawn_b_coord[0]) == 1:
        if abs(pawn_w_coord[1]-pawn_b_coord[1]) == 1:
            if current_pawn == 'w':
                print(f"Game over! White win, capture on {chess_board[pawn_b_coord[0]][pawn_b_coord[1]]}.")
                break
            elif current_pawn == 'b':
                print(f"Game over! Black win, capture on {chess_board[pawn_w_coord[0]][pawn_w_coord[1]]}.")
                break
    if current_pawn == 'w':
        pawn_w_coord[0] -= 1
        if pawn_w_coord[0] == 0:
            print(
                f"Game over! White pawn is promoted to a queen at {chess_board[pawn_w_coord[0]][pawn_w_coord[1]]}.")
            break
    if current_pawn == 'b':
        pawn_b_coord[0] += 1
        if pawn_b_coord[0] == size - 1:
            print(
                f"Game over! Black pawn is promoted to a queen at {chess_board[pawn_b_coord[0]][pawn_b_coord[1]]}.")
            break
    pawns[0], pawns[1] = pawns[1], pawns[0]


