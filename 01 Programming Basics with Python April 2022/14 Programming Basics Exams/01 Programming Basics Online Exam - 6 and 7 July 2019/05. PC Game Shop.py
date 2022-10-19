sold_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0


for _ in range(sold_games):
    game_name = input()
    if game_name == 'Hearthstone':
        hearthstone +=1
    elif game_name == 'Fornite':
        fornite +=1
    elif game_name == 'Overwatch':
        overwatch +=1
    else:
        others +=1

hearthstone_perc = hearthstone / sold_games * 100
fornite_perc = fornite / sold_games * 100
overwatch_perc = overwatch / sold_games * 100
others_perc = others / sold_games * 100

print(f"Hearthstone - {hearthstone_perc:.2f}%")
print(f"Fornite - {fornite_perc:.2f}%")
print(f"Overwatch - {overwatch_perc:.2f}%")
print(f"Others - {others_perc:.2f}%")

