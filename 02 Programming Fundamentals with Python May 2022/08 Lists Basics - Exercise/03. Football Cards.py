list_cards = input().split()
list_team_a = []
list_team_b = []
is_game_terminated = False
for i in range(1, 12):
    list_team_a.append('A-'+str(i))
for i in range(1, 12):
    list_team_b.append('B-'+str(i))
for element in list_cards:
    if element in list_team_a:
        list_team_a.remove(element)
    elif element in list_team_b:
        list_team_b.remove(element)
    if len(list_team_a) < 7 or len(list_team_b) < 7:
        is_game_terminated = True
        break
print(f"Team A - {len(list_team_a)}; Team B - {len(list_team_b)}")
if is_game_terminated:
    print("Game was terminated")