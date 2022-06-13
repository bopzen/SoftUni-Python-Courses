def min_max_sum(list_numbers):
    list_numbers = list(map(int,list_numbers))
    min_value = min(list_numbers)
    max_value = max(list_numbers)
    sum_value = sum(list_numbers)
    print(f"The minimum number is {min_value}")
    print(f"The maximum number is {max_value}")
    print(f"The sum number is: {sum_value}")


numbers = input().split()
min_max_sum(numbers)