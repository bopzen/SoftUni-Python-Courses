import re

search_pattern = r"\d+"
line = input()
while True:
    if line:
        result = re.findall(search_pattern, line)
        if result:
            print(" ".join(result), end=" ")
        line = input()
    else:
        break