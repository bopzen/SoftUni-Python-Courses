list_rooms = input().split("|")
health = 100
bitcoins = 0
is_dead = False
best_room = 1
for room in list_rooms:
    command_number = room.split()
    command = command_number[0]
    number = int(command_number[1])
    if command == 'potion':
        if health + number > 100:
            heal = 100 - health
        else:
            heal = number
        health += heal
        print(f"You healed for {heal} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            is_dead = True
            break
        else:
            print(f"You slayed {command}.")
    best_room += 1
if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
