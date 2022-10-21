import re

search_pattern = r"([#|\|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
text = input()
total_calories = 0
result = re.finditer(search_pattern, text)
for match in result:
    calories = int(match.group(4))
    total_calories += calories
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
result = re.finditer(search_pattern, text)
for match in result:
    print(f"Item: {match[2]}, Best before: {match[3]}, Nutrition: {match[4]}")