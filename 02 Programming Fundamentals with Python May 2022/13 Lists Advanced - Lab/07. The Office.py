list_happiness = list(map(int, input().split()))
factor = int(input())
list_happiness_with_factor = list(map(lambda x: x * factor, list_happiness))
average = sum(list_happiness_with_factor) / len(list_happiness_with_factor)
list_happiness_above_average = list(filter(lambda x: x >= average, list_happiness_with_factor))
if len(list_happiness_above_average) >= len(list_happiness_with_factor) / 2:
    print(f"Score: {len(list_happiness_above_average)}/{len(list_happiness_with_factor)}. Employees are happy!")
else:
    print(f"Score: {len(list_happiness_above_average)}/{len(list_happiness_with_factor)}. Employees are not happy!")