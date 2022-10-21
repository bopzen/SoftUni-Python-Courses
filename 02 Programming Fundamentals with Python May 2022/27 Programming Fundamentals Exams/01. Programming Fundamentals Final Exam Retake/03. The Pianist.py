n = int(input())
pieces_dict = {}
for _ in range(n):
    pieces = input().split("|")
    piece, composer, key = pieces[0], pieces[1], pieces[2]
    pieces_dict[piece] = {}
    pieces_dict[piece][composer] = key

while True:
    command = input()
    if command == 'Stop':
        break
    list_command = command.split("|")
    action = list_command[0]
    if action == 'Add':
        piece, composer, key = list_command[1], list_command[2], list_command[3]
        if piece not in pieces_dict:
            pieces_dict[piece] = {}
            pieces_dict[piece][composer] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == 'Remove':
        piece = list_command[1]
        if piece in pieces_dict:
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == 'ChangeKey':
        piece, new_key = list_command[1], list_command[2]
        if piece in pieces_dict:
            done = False
            for key, value in pieces_dict.items():
                for nested_key, nested_value in value.items():
                    if key == piece:
                        pieces_dict[key][nested_key] = new_key
                        done = True
                        print(f"Changed the key of {piece} to {new_key}!")
                        break
                if done:
                    break
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in pieces_dict.items():
    for nested_key, nested_value in value.items():
        print(f"{key} -> Composer: {nested_key}, Key: {nested_value}")

