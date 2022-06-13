num1 = int(input())
num2 = int(input())

for i in range(num1,num2+1):
    i = str(i)
    sum_even = 0
    sum_odd = 0
    for index, value in enumerate(i):
        if index % 2 == 0:
            sum_even += int(value)
        else:
            sum_odd += int(value)
    if sum_even == sum_odd:
        print(i, end= ' ')