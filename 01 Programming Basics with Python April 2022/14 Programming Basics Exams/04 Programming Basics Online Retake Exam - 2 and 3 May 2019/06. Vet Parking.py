days = int(input())
hours = int(input())
total_amount = 0
for d in range(1, days+1):
    day_amount = 0
    for h in range(1, hours+1):
        if d % 2 == 0 and h % 2 != 0:
            price = 2.5
        elif d % 2 != 0 and h % 2 == 0:
            price = 1.25
        else:
            price = 1
        day_amount += price
    total_amount += day_amount
    print(f'Day: {d} - {day_amount:.2f} leva')
print(f'Total: {total_amount:.2f} leva')