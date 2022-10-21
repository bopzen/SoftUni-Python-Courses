list_treasure = input().split("|")

while True:
    command = input()
    if command == 'Yohoho!':
        break
    list_command = command.split()
    action = list_command[0]
    if action == 'Loot':
        for index in range(1, len(list_command)):
            if list_command[index] not in list_treasure:
                list_treasure.insert(0,list_command[index])
    elif action == 'Drop':
        index = int(list_command[1])
        if 0 <= index <= len(list_treasure)-1:
            move = list_treasure[index]
            list_treasure.pop(index)
            list_treasure.append(move)
        else:
            continue
    elif action == 'Steal':
        count = int(list_command[1])
        list_stolen = []
        start = max(len(list_treasure) - count, 0)
        list_stolen = list_treasure[start::1]
        list_treasure = list_treasure[:start:1]
        print(", ".join(list_stolen))
count_items = len(list_treasure)
if count_items == 0:
    print("Failed treasure hunt.")
else:
    string_treasure = "".join(list_treasure)
    length_string_treasure = len(string_treasure)
    average_treasure_gain = length_string_treasure / count_items
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
