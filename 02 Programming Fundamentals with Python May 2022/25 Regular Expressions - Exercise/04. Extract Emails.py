import re

text = input()
search_pattern = r"(?<=\s)(([a-z0-9]+[\.\-_a-z0-9])*@[\-a-z]+(\.[a-z]+)+)\b"
result = re.findall(search_pattern, text)
for match in result:
    print(match[0])