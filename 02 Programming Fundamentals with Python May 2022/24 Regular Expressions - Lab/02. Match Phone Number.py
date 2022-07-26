import re

phone_numbers = input()
search_pattern = r"\+359([\s-])2(\1)\d{3}(\1)\d{4}\b"
result = re.finditer(search_pattern, phone_numbers)
print(", ".join([match.group() for match in result]))