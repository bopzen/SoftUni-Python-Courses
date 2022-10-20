player1 = input()
player2 = input()
number_wars1 = 0
number_wars2 = 0
player1_points = 0
player2_points = 0

while number_wars1 == number_wars2:
    player1_card = input()
    if player1_card == 'End of game':
        print(f"{player1} has {player1_points} points")
        print(f"{player2} has {player2_points} points")
        break
    player2_card = int(input())
    player1_card = int(player1_card)
    if player1_card > player2_card:
        player1_points += player1_card - player2_card
    elif player2_card > player1_card:
        player2_points += player2_card - player1_card
    else:
        number_wars1 = int(input())
        number_wars2 = int(input())
        print("Number wars!")
        if number_wars1 > number_wars2:
            print(f"{player1} is winner with {player1_points} points")
        else:
            print(f"{player2} is winner with {player2_points} points")