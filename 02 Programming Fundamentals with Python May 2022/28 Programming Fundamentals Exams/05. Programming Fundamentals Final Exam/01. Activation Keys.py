activation_key = input()
while True:
    command = input()
    if command == 'Generate':
        break
    tokens = command.split(">>>")
    action = tokens[0]
    if action == 'Contains':
        substring = tokens[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == 'Flip':
        case, start_index, end_index = tokens[1], int(tokens[2]), int(tokens[3])
        flipped_string = ""
        for i in range(start_index, end_index):
            if case == 'Upper':
                flipped_string += activation_key[i].upper()
            elif case == 'Lower':
                flipped_string += activation_key[i].lower()
        activation_key = activation_key[:start_index] + flipped_string + activation_key[end_index:]
        print(activation_key)
    elif action == 'Slice':
        start_index, end_index = int(tokens[1]), int(tokens[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
print(f"Your activation key is: {activation_key}")