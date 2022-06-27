n = int(input())
field = [list(map(int,input().split())) for _ in range(n)]
attacks = input().split()
count_destroyed_ships = 0
for element in attacks:
    attack_coordinates = element.split("-")
    attack_row = int(attack_coordinates[0])
    attack_column = int(attack_coordinates[1])
    if field[attack_row][attack_column] > 0:
        field[attack_row][attack_column] -= 1
        if field[attack_row][attack_column] == 0:
            count_destroyed_ships += 1
    elif field[attack_row][attack_column] == 0:
        continue
print(count_destroyed_ships)