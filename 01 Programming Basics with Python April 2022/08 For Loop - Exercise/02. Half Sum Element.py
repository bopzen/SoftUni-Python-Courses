n = int(input())
sum_previous = 0
max_num = -10000000
for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_previous += num
diff = abs(sum_previous - 2 * max_num)
if diff == 0:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {diff}')