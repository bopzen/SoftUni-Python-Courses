list_numbers = list(map(int, input().split(", ")))
list_even_indices = list(map(lambda x: x if list_numbers[x] % 2 == 0 else 'no', range(len(list_numbers))))
print(list(filter(lambda a: a != 'no', list_even_indices)))
