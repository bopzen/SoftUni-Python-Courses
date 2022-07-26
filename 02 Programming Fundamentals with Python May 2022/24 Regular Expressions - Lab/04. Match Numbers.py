import re

dates = input()
search_pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
result = re.finditer(search_pattern, dates)
for match in result:
    print(match.group(), end=" ")