n = int(input())
is_odd = False
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        is_odd = True
        break
if is_odd:
    print(f'{number} is odd!')
else:
    print('All numbers are even.')