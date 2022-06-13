list_numbers = input().split()
text = input()
list_text = []
for element in text:
    list_text.append(element)

for element in list_numbers:
    sum = 0
    for i in element:
        sum += int(i)
    if sum > len(list_text):
        index = sum % len(list_text)
        char = list_text[index]
    else:
        index = sum
        char = list_text[index]
    print(char, end='')
    list_text.pop(index)