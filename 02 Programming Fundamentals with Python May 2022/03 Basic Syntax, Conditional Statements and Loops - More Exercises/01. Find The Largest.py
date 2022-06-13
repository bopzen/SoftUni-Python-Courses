number = input()
list_number = []
for element in number:
    list_number.append(int(element))
list_number.sort(reverse=True)
for element in list_number:
    print(element,end='')