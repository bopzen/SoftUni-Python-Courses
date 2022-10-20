count_wins = 0
count_losses = 0
count_games = 0
count_tournament_games = 0
while True:
    tournament = input()
    if tournament == 'End of tournaments':
        break
    games = int(input())
    for g in range(games):
        count_games += 1
        count_tournament_games += 1
        desi_team_points = int(input())
        other_team_points = int(input())
        if desi_team_points > other_team_points:
            count_wins += 1
            print(f"Game {count_tournament_games} of tournament {tournament}: win with {abs(desi_team_points-other_team_points)} points.")
        elif desi_team_points < other_team_points:
            count_losses +=1
            print(f"Game {count_tournament_games} of tournament {tournament}: lost with {abs(desi_team_points-other_team_points)} points.")
    count_tournament_games = 0
print(f"{count_wins/count_games*100:.2f}% matches win")
print(f"{count_losses/count_games*100:.2f}% matches lost")
