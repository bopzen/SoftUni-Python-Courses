list_text = input()
chars_dict = {}
for ch in list_text:
    if ch == " ":
        continue
    if ch not in chars_dict:
        chars_dict[ch] = 1
    else:
        chars_dict[ch] += 1

print("\n".join(f"{key} -> {value}" for key, value in chars_dict.items()))