list_text = input().split()
total = 0
for text in list_text:
    result = 0
    first_letter = text[0]
    last_letter = text[-1]
    number = int(text[1:-1])
    first_letter_position = ord(first_letter.upper()) - 64
    last_letter_position = ord(last_letter.upper()) - 64
    if first_letter.isupper():
        result += number / first_letter_position
    elif first_letter.islower():
        result += number * first_letter_position
    if last_letter.isupper():
        result -= last_letter_position
    elif last_letter.islower():
        result += last_letter_position
    total += result
print(f"{total:.2f}")