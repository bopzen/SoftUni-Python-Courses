force_dict = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if " | " in command:
        list_command = command.split(" | ")
        force_side, force_user = list_command[0], list_command[1]
        if force_user not in [element for value in force_dict.values() for element in value] and force_side not in force_dict:
            force_dict[force_side] = [force_user]
        elif force_user not in [element for value in force_dict.values() for element in value] and force_side in force_dict:
            force_dict[force_side].append(force_user)
    elif " -> " in command:
        list_command = command.split(" -> ")
        force_user, force_side = list_command[0], list_command[1]
        if force_user not in [element for value in force_dict.values() for element in value] and force_side not in force_dict:
            force_dict[force_side] = [force_user]
            print(f"{force_user} joins the {force_side} side!")
        elif force_user not in [element for value in force_dict.values() for element in value] and force_side in force_dict:
            force_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        elif force_user in [element for value in force_dict.values() for element in value]:
            for key, value in force_dict.items():
                if force_user in value:
                    index = value.index(force_user)
                    if force_side not in force_dict:
                        force_dict[force_side] = [value.pop(index)]
                    else:
                        force_dict[force_side].append(value.pop(index))
                    print(f"{force_user} joins the {force_side} side!")
                    break

for key, value in force_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for element in value:
            print(f"! {element}")
