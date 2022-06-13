text = input().lower()
list_items = ['sand', 'water', 'fish', 'sun']
counter = 0
for item in list_items:
    counter += text.count(item)

print(counter)