text = input()
list_upper = []

for index in range(len(text)):
    if 65 <= ord(text[index]) <= 90:
        list_upper.append(index)
print(list_upper)