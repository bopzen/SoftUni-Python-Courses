def create_table(rows, columns):
    table = []
    for i in range(rows):
        table.append([])
        for j in range(columns):
            table[i].append('0')
    return table


def print_table(table):
    print()
    [print(*row) for row in table]


def take_turn(player):
    try:
        col = int(input(f"\n{player}, please choose your column: ")) - 1
    except ValueError:
        print(f'Enter numbers only!')
        return take_turn(player)
    for row in range(len(current_table)-1, -1, -1):
        try:
            if current_table[row][col] == '0':
                current_table[row][col] = player[-1]
                break
        except IndexError:
            print(f'Enter valid value between 1 and {table_cols}!')
            return take_turn(player)
    else:
        print('No more spaces left')
        return take_turn(player)


def check_draw():
    for row in current_table:
        if '0' in row:
            return False
    return True


def check_winner(player):
    for row in range(table_rows):
        for col in range(table_cols):
            if current_table[row][col] == player[-1]:
                for coordinates in directions:
                    check_row, check_col = row, col
                    for _ in range(3):
                        check_row += coordinates[0]
                        check_col += coordinates[1]
                        if not 0 <= check_row < table_rows or not 0 <= check_col < table_cols:
                            break
                        if current_table[check_row][check_col] != player[-1]:
                            break
                    else:
                        return True
    return False


def play_another_game():
    another_game = input('Do you want another game Y/N: ')
    if another_game.upper() == 'Y':
        return True
    elif another_game.upper() == 'N':
        return False
    else:
        print('Enter Y or N!')
        return play_another_game()


table_rows = 6
table_cols = 7
directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]

while True:
    players = ['Player1', 'Player2']
    current_table = create_table(table_rows, table_cols)
    print_table(current_table)

    while True:
        current_player = players[0]
        take_turn(current_player)
        print_table(current_table)
        if check_draw():
            print(f"It's a draw. No one wins!")
            break
        if check_winner(current_player):
            print(f'Winner is {current_player}')
            break
        players[0], players[1] = players[1], players[0]

    if play_another_game():
        continue
    else:
        break


