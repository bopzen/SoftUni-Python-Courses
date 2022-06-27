message = input()
list_numbers = []
list_non_numbers = []
for element in message:
    if element.isdigit():
        list_numbers.append(element)
    else:
        list_non_numbers.append(element)
take_list = [list_numbers[x] for x in range(len(list_numbers)) if x % 2 == 0]
skip_list = [list_numbers[x] for x in range(len(list_numbers)) if x % 2 != 0]
start_index = 0
end_index = 0
result = []
for i in range(len(take_list)):
    end_index = start_index + int(take_list[i])
    result.extend(list_non_numbers[start_index:end_index])
    start_index = end_index + int(skip_list[i])
print("".join(result))