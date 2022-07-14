list_keys = list(map(int, input().split()))
list_text = []
length_keys = len(list_keys)

while True:
    command = input()
    if command == 'find':
        break
    list_text.append(command)

for text in list_text:
    counter_key = 0
    decrypted_text = ""
    for ch in text:
        if counter_key == length_keys:
            counter_key = 0
        decrypted_text += chr(ord(ch)-list_keys[counter_key])
        counter_key += 1
    treasure = ""
    coordinates = ""
    is_treasure_found = False
    is_coordinates_found = False
    for ch in decrypted_text:
        if ch == "&" and is_treasure_found:
            is_treasure_found = False
        elif ch == "&" and not is_treasure_found:
            is_treasure_found = True
        if is_treasure_found and ch != "&":
            treasure += ch
        if is_coordinates_found and ch != ">":
            coordinates += ch
        if ch == "<":
            is_coordinates_found = True
        if ch == ">":
            is_coordinates_found = False

    print(f"Found {treasure} at {coordinates}")