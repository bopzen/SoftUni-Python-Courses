import math
player_one = None
player_two = None
current_board = [[" "," "," ",], [" "," "," ",], [" "," "," ",]]


def set_players():
    global player_one, player_two
    player1_name = input('Player One Name: ')
    player2_name = input('Player Two Name: ')
    while True:
        player1_sign = input(f"{player1_name} would you like to play with 'X' or 'O'? ").upper()
        if player1_sign not in 'XO':
            print("Enter 'X' or 'O' only")
            continue
        else:
            break
    player2_sign = 'X' if player1_sign == 'O' else 'O'

    player_one = [player1_name, player1_sign]
    player_two = [player2_name, player2_sign]


def start_game():
    print("This is the numeration of the board:")
    print("|  1  |  2  |  3  |")
    print("|  4  |  5  |  6  |")
    print("|  7  |  8  |  9  |")
    print(f"{player_one[0]} starts first!")


def print_board(board):
    for row in board:
        print("|  ", end="")
        print("  |  ".join(x for x in row), end="")
        print("  |")


def make_turn(player):
    while True:
        try:
            choice = int(input(f"{player[0]} choose a free position [1-9]: "))
        except ValueError:
            print('Enter number between 1 and 9!')
            continue
        if 1 <= choice <= 9:
            row = math.ceil(choice / 3) - 1
            col = choice % 3 - 1
            if current_board[row][col] == " ":
                current_board[row][col] = current_player[1]
                break
            else:
                print('The position is already taken. Please try again!')
        else:
            print('Enter valid number!')

    row = math.ceil(choice/3) - 1
    col = choice % 3 -1
    current_board[row][col] = current_player[1]


def check_win(player):
    result = False
    first_diagonal_win = all([current_board[i][i] == player[1] for i in range(3)])
    second_diagonal_win = all([current_board[i][2 - i] == player[1] for i in range(3)])
    row_win = any([all(True if pos == player[1] else False for pos in row) for row in current_board])
    col_win = any([all(True if current_board[r][c] == player[1] else False for r in range(3)) for c in range(3)])
    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print(f'{player[0]} won!')
        result = True
    return result


set_players()
start_game()
players = [player_one, player_two]
current_player = players[0]
print_board(current_board)


while True:
    current_player = players[0]
    make_turn(current_player)
    print_board(current_board)
    if check_win(current_player):
        break
    players[0], players[1] = players[1], players[0]