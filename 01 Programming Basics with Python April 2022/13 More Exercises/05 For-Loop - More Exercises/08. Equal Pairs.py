n = int(input())
max_diff = -100000
for i in range(n):
    num1 = int(input())
    num2 = int(input())
    if i == 0 and n == 1:
        sum_previous = num1 + num2
        max_diff = 0
    elif i == 0 and n >1:
        sum_previous = num1 + num2
    else:
        sum = num1 + num2
        diff = abs(sum-sum_previous)
        if diff > max_diff :
            max_diff = diff
        sum_previous = sum
if max_diff == 0:
    print(f'Yes, value={sum_previous}')
else:
    print(f'No, maxdiff={max_diff}')