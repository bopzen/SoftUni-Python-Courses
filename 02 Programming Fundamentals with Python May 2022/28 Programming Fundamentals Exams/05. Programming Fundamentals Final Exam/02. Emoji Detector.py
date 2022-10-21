import re
text = input()
search_pattern = r"(::|\*\*)(?P<emoji>[A-Z][a-z]{2}[a-z]*)(\1)"
search_pattern_digits = r"\d"
digits = re.findall(search_pattern_digits, text)
cool_threshold = 1
for element in digits:
    cool_threshold *= int(element)
print(f"Cool threshold: {cool_threshold}")

result = re.finditer(search_pattern, text)
count_emojis = 0
for match in result:
    count_emojis += 1
print(f"{count_emojis} emojis found in the text. The cool ones are:")
result = re.finditer(search_pattern, text)
for match in result:
    emoji = match.group('emoji')
    sum_letters = 0
    for ch in emoji:
        sum_letters += ord(ch)
    if sum_letters >= cool_threshold:
        print("".join(match.groups()))