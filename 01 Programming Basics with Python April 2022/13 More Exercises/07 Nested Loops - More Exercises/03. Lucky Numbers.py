n = int(input())
for number in range(1000,10000):
    is_zero = False
    number = str(number)
    for i in number:
        if i == str(0):
            is_zero = True
            break
    if is_zero:
        continue
    sum_first = 0
    sum_last = 0
    for index, value in enumerate(number):
        if index == 0 or index == 1:
            sum_first += int(value)
        elif index == 2 or index == 3:
            sum_last += int(value)
    if sum_first == sum_last and n % sum_first == 0:
        print(number, end=' ')