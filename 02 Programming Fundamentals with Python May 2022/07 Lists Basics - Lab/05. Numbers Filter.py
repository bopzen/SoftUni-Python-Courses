n = int(input())
numbers_list = []
numbers_list_filtered = []
for _ in range(n):
    number = int(input())
    numbers_list.append(number)
command = input()
if command == 'even':
    for element in numbers_list:
        if element % 2 == 0 or element == 0:
            numbers_list_filtered.append(element)
elif command == 'odd':
    for element in numbers_list:
        if element % 2 != 0:
            numbers_list_filtered.append(element)
elif command == 'negative':
    for element in numbers_list:
        if element < 0:
            numbers_list_filtered.append(element)
elif command == 'positive':
    for element in numbers_list:
        if element >= 0:
            numbers_list_filtered.append(element)
print(numbers_list_filtered)