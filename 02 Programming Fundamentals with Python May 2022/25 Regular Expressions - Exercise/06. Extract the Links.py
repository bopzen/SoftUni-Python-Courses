import re
valid_url = []
search_pattern = r"(www\.[A-Za-z0-9-]+\.[a-z]+(\.[a-z]+)*)"
text = input()
while text:

    result = re.search(search_pattern, text)
    if result:
        valid_url.append(result.group(1))
    text = input()
for element in valid_url:
    print(element)
