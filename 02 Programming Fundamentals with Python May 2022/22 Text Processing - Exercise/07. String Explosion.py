text = input()
new_text = ""
strength = 0
for i in range(len(text)):
    if text[i] == ">":
        strength += int(text[i+1])
        new_text += text[i]
    else:
        if strength > 0:
            strength -= 1
            continue
        else:
            new_text += text[i]

print(new_text)