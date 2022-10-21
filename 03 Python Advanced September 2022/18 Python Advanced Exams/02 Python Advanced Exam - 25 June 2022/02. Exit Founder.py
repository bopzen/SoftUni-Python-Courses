names = input().split(', ')
size = 6
maze = [input().split() for i in range(size)]
rest_players = []
rest = False

while True:
    coordinates = input()[1:-1].split(", ")
    x, y = int(coordinates[0]), int(coordinates[1])
    current_player = names[0]
    if current_player in rest_players:
        rest_players.remove(current_player)
        names[0], names[1] = names[1], names[0]
        continue
    if maze[x][y] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif maze[x][y] == 'T':
        print(f"{current_player} is out of the game! The winner is {names[1]}.")
        break
    elif maze[x][y] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        rest_players.append(current_player)
    names[0], names[1] = names[1], names[0]