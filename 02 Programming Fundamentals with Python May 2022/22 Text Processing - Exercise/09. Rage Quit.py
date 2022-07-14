text = input()
rage_quit_text = ""
temp_text = ""
temp_digit = ""
unique_symbols = []
for ch in text:
    if ch.isdigit():
        temp_digit += ch
    else:
        if temp_digit != "":
            rage_quit_text += temp_text * int(temp_digit)
            temp_text = ""
            temp_text += ch.upper()
            temp_digit = ""
        else:
            temp_text += ch.upper()
        if ch.upper() not in unique_symbols:
            unique_symbols.append(ch.upper())
if temp_digit != "":
    rage_quit_text += temp_text * int(temp_digit)
print(f"Unique symbols used: {len(unique_symbols)}")
print(rage_quit_text)