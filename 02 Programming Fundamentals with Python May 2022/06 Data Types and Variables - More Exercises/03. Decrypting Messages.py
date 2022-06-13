key = int(input())
lines = int(input())
message = ""
for i in range(lines):
    character = input()
    new_character = ord(character) + key
    message += chr(new_character)
print(message)