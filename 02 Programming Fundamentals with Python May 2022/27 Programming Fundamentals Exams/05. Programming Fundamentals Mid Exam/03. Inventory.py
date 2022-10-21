list_items = input().split(", ")

while True:
    command = input()
    if command == 'Craft!':
        break
    list_command = command.split(" - ")
    action = list_command[0]
    if action == 'Collect':
        item = list_command[1]
        if item in list_items:
            continue
        list_items.append(item)
    elif action == 'Drop':
        item = list_command[1]
        if item in list_items:
            list_items.remove(item)
    elif action == 'Combine Items':
        list_old_new_items = list_command[1].split(":")
        old_item = list_old_new_items[0]
        new_item = list_old_new_items[1]
        if old_item in list_items:
            list_items.insert(list_items.index(old_item)+1, new_item)
    elif action == 'Renew':
        item = list_command[1]
        if item in list_items:
            list_items.append(list_items.pop(list_items.index(item)))
print(", ".join(list_items))