n = int(input())
word = input()
text_list = []
text_list_filtered = []
for _ in range(n):
    text = input()
    text_list.append(text)
print(text_list)
for element in text_list:
    if word in element:
        text_list_filtered.append(element)
print(text_list_filtered)