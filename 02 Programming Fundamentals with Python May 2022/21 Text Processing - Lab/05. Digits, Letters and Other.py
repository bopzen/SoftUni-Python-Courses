text = input()
digits = ""
letters = ""
chars = ""
for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        chars += ch
print(digits)
print(letters)
print(chars)