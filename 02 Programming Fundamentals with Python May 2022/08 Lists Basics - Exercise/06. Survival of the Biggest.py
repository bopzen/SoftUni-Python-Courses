list_numbers_str = input().split()
numbers_to_remove = int(input())
list_numbers = []
for element in list_numbers_str:
    list_numbers.append(int(element))
for element in range(numbers_to_remove):
    list_numbers.remove(min(list_numbers))

for index in range(len(list_numbers)-1):
    print(list_numbers[index], end=', ')
print(list_numbers[-1])