team_name = input()
games = int(input())
wins = 0
draws = 0
losses = 0
points = 0
if games >0:
    for _ in range(games):
        result = input()
        if result == 'W':
            wins +=1
            points +=3
        elif result == 'D':
            draws +=1
            points +=1
        elif result == 'L':
            losses +=1

    print(f"{team_name} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}" )
    print(f"## L: {losses}" )
    print(f"Win rate: {wins/games*100:.2f}%")


else:

    print(f"{team_name} hasn't played any games during this season.")
