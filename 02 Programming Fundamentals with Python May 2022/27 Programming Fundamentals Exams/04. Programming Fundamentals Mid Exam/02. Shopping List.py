list_groceries = input().split("!")

while True:
    command = input()
    if command == 'Go Shopping!':
        break
    list_command = command.split()
    if list_command[0] == 'Urgent':
        item = list_command[1]
        if item in list_groceries:
            continue
        else:
            list_groceries.insert(0, item)
    elif list_command[0] == 'Unnecessary':
        item = list_command[1]
        if item in list_groceries:
            list_groceries.remove(item)
        else:
            continue
    elif list_command[0] == 'Correct':
        old_item = list_command[1]
        new_item = list_command[2]
        if old_item in list_groceries:
            index = list_groceries.index(old_item)
            list_groceries[index] = new_item
        else:
            continue
    elif list_command[0] == 'Rearrange':
        item = list_command[1]
        if item in list_groceries:
            list_groceries.remove(item)
            list_groceries.append(item)
        else:
            continue
print(", ".join(list_groceries))