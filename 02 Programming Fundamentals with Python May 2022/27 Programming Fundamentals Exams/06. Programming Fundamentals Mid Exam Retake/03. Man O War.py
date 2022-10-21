list_pirate_ship = list(map(int,input().split(">")))
list_war_ship = list(map(int,input().split(">")))
max_health = int(input())
is_war_ship_sunk = False
is_pirate_ship_sunk = False
while True:
    command = input()
    if command == 'Retire':
        break
    list_command = command.split()
    action = list_command[0]
    if action == 'Fire':
        index = int(list_command[1])
        damage = int(list_command[2])
        if 0 <= index < len(list_war_ship):
            list_war_ship[index] -= damage
            if list_war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_war_ship_sunk = True
                break
        else:
            continue
    elif action == 'Defend':
        start_index = int(list_command[1])
        end_index = int(list_command[2])
        damage = int(list_command[3])
        if start_index >= 0 and end_index < len(list_pirate_ship):
            for i in range(start_index, end_index+1):
                list_pirate_ship[i] -= damage
                if list_pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_pirate_ship_sunk = True
                    break
        else:
            continue
    elif action == 'Repair':
        index = int(list_command[1])
        health = int(list_command[2])
        if 0 <= index < len(list_pirate_ship):
            list_pirate_ship[index] = min(list_pirate_ship[index]+health,max_health)
        else:
            continue
    elif action == 'Status':
        count_repair = len(list(filter(lambda x: x < max_health * 0.2, list_pirate_ship)))
        print(f"{count_repair} sections need repair.")
    if is_war_ship_sunk or is_pirate_ship_sunk:
        break
if command == 'Retire':
    print(f"Pirate ship status: {sum(list_pirate_ship)}")
    print(f"Warship status: {sum(list_war_ship)}")