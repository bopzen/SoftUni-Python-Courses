list_hearts = list(map(int,input().split("@")))
position = 0
while True:
    command = input()
    if command == 'Love!':
        break
    list_command = command.split()
    jump_length = int(list_command[1])
    position += jump_length
    if position >= len(list_hearts):
        position = 0
    if list_hearts[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        list_hearts[position] -= 2
        if list_hearts[position] == 0:
            print(f"Place {position} has Valentine's day.")
print(f"Cupid's last position was {position}.")
if sum(list_hearts) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(list(filter(lambda x: x != 0,list_hearts)))} places.")