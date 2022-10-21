text = input()

while True:
    command = input()
    if command == 'Reveal':
        break
    tokens = command.split(":|:")
    action = tokens[0]
    if action == 'InsertSpace':
        index = int(tokens[1])
        text = text[:index] + " " + text[index:]
        print(text)
    elif action == 'Reverse':
        substring = tokens[1]
        if substring in text:
            text = text.replace(substring, "", 1)
            text += substring[::-1]
            print(text)
        else:
            print("error")
    elif action == 'ChangeAll':
        substring, replacement = tokens[1], tokens[2]
        text = text.replace(substring, replacement)
        print(text)
print(f"You have a new text message: {text}")
