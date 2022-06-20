list_numbers = list(map(int,input().split()))
sum_values = 0
while len(list_numbers) > 0:
    index = int(input())
    if index < 0:
        remove_value = list_numbers[0]
        copy_value = list_numbers[-1]
        list_numbers[0] = copy_value
    elif index > len(list_numbers)-1:
        remove_value = list_numbers[-1]
        copy_value = list_numbers[0]
        list_numbers[-1] = copy_value
    else:
        remove_value = list_numbers[index]
        list_numbers.pop(index)
    list_numbers = list(map(lambda x: x+remove_value if x <= remove_value else x-remove_value, list_numbers))
    sum_values += remove_value
print(sum_values)