def between_chars(char1, char2):
    text = ''
    for i in range(ord(char1)+1,ord(char2)):
        text += f'{chr(i)} '
    return text


character1 = input()
character2 = input()

print(between_chars(character1, character2))