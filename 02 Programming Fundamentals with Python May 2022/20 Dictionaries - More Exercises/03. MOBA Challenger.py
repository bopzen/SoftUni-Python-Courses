player_stats = {}

while True:
    command = input()
    if command == 'Season end':
        break
    if '->' in command:
        list_command = command.split(' -> ')
        player, position, skill = list_command[0], list_command[1], int(list_command[2])
        if player not in player_stats:
            player_stats[player] = {}
            player_stats[player][position] = skill
        else:
            if position in player_stats[player]:
                if skill > player_stats[player][position]:
                    player_stats[player][position] = skill
            else:
                player_stats[player][position] = skill
    if ' vs ' in command:
        list_command = command.split(' vs ')
        player1, player2 = list_command[0], list_command[1]
        common_position = False
        if player1 in player_stats and player2 in player_stats:
            for position1 in player_stats[player1]:
                for position2 in player_stats[player2]:
                    if position1 == position2:
                        common_position = True
                        break
                if common_position:
                    break
            if common_position:
                total_skills_player1 = sum(skill for skill in player_stats[player1].values())
                total_skills_player2 = sum(skill for skill in player_stats[player2].values())
                if total_skills_player1 > total_skills_player2:
                    del player_stats[player2]
                elif total_skills_player2 > total_skills_player1:
                    del player_stats[player1]
player_total_skills = {}
for key, value in player_stats.items():
    total = 0
    for nested_values in value.values():
        total += nested_values
    player_total_skills[key] = total

for key, value in sorted(player_total_skills.items(), key=lambda x: -x[1]):
    print(f"{key}: {value} skill")
    for position, skill in sorted(player_stats[key].items(), key=lambda x: (-x[1],x[0])):
        print(f"- {position} <::> {skill}")
