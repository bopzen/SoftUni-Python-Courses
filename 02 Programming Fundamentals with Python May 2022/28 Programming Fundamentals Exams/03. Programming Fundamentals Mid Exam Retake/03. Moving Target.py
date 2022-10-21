list_targets = list(map(int, input().split()))

while True:
    command = input()
    if command == 'End':
        break
    list_command = command.split()
    action = list_command[0]
    if action == 'Shoot':
        index = int(list_command[1])
        power = int(list_command[2])
        if index < 0 or index >= len(list_targets):
            continue
        list_targets[index] -= power
        if list_targets[index] <= 0:
            list_targets.pop(index)
    elif action == 'Add':
        index = int(list_command[1])
        value = int(list_command[2])
        if index < 0 or index >= len(list_targets):
            print("Invalid placement!")
            continue
        list_targets.insert(index, value)
    elif action == 'Strike':
        index = int(list_command[1])
        radius = int(list_command[2])
        if index - radius >= 0 and index + radius < len(list_targets):
            for i in range(index+radius, index - radius -1, -1):
                list_targets.pop(i)
        else:
            print("Strike missed!")
            continue
print("|".join(map(str,list_targets)))