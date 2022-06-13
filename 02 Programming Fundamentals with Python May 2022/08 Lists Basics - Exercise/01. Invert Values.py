list_strings = input().split()
list_strings_inverted = []
for element in list_strings:
    list_strings_inverted.append(-int(element))

print(list_strings_inverted)