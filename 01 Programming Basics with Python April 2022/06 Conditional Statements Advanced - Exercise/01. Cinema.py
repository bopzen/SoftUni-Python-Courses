type = input()
rows = int(input())
columns = int(input())
seats = rows * columns
if type == 'Premiere':
    income = seats * 12
elif type == 'Normal':
    income = seats * 7.5
elif type == 'Discount':
    income = seats * 5
print(f'{income:.2f} leva')