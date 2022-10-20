best_player = ''
best_player_goals = 0
goals = 0
has_hattrick = False
while goals <10:
    player = input()
    if player == 'END':
        break
    goals = int(input())
    if goals > best_player_goals:
        best_player = player
        best_player_goals = goals
    if best_player_goals >=3:
        has_hattrick = True
print(f"{best_player} is the best player!")
if has_hattrick:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")