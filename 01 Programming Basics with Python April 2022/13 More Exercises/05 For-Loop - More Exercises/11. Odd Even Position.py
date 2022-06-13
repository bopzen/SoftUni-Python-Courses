n = int(input())
sum_odd = 0
sum_even = 0
min_odd = 1000000
max_odd = -1000000
min_even = 1000000
max_even = -1000000
for i in range(1,n+1):
    num = float(input())
    if i % 2 == 0:
        sum_even += num
        if num > max_even:
            max_even = num
        if num < min_even:
            min_even = num
    else:
        sum_odd += num
        if num > max_odd:
            max_odd = num
        if num < min_odd:
            min_odd = num
print(f'OddSum={sum_odd:.2f},')
if min_odd == 1000000:
    print(f'OddMin=No,')
else:
    print(f'OddMin={min_odd:.2f},')
if max_odd == -1000000:
    print(f'OddMax=No,')
else:
    print(f'OddMax={max_odd:.2f},')

print(f'EvenSum={sum_even:.2f},')
if min_even == 1000000:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={min_even:.2f},')
if max_even == -1000000:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={max_even:.2f}')