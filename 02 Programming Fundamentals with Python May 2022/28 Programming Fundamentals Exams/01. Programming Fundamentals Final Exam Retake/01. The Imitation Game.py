encrypted_message = input()

while True:
    command = input()
    if command == 'Decode':
        break
    tokens = command.split("|")
    action = tokens[0]
    if action == 'Move':
        num_letters = int(tokens[1])
        encrypted_message = encrypted_message[num_letters:] + encrypted_message[:num_letters]
    elif action == 'Insert':
        index, value = int(tokens[1]), tokens[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == 'ChangeAll':
        substring, replacement = tokens[1], tokens[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")
    print(" ".join(list_memory_elements))


