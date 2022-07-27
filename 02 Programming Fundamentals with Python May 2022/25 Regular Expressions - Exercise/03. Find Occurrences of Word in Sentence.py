import re

text = input()
word = input()
search_pattern = rf"\b{word}\b"
result = re.findall(search_pattern, text, flags=re.IGNORECASE)
print(len(result))