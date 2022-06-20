text1 = input().split(", ")
text2 = input().split(", ")
filtered_text1 = []
for element1 in text1:
    for element2 in text2:
        if element1 in element2:
            filtered_text1.append(element1)
            break
print(filtered_text1)