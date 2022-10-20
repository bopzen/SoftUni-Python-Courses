player_name = input()
points_left = 301
counter_shots = 0
counter_fails = 0
command = input()
while command != 'Retire':
    points = int(input())
    if command == 'Single':
        points = points
    elif command == 'Double':
        points = points * 2
    elif command == 'Triple':
        points = points * 3
    if points > points_left:
        counter_fails += 1
        command = input()
        continue
    points_left -= points
    counter_shots += 1
    if points_left == 0:
        break
    command = input()
if points_left == 0:
    print(f"{player_name} won the leg with {counter_shots} shots.")
else:
    print(f"{player_name} retired after {counter_fails} unsuccessful shots.")
