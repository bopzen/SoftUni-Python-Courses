season = input()
km_per_month = float(input())
km_per_season = km_per_month * 4
profit = 0
if km_per_month <=5000:
    if season == 'Spring' or season == 'Autumn':
        profit = km_per_season * 0.75
    elif season == 'Summer':
        profit = km_per_season * 0.9
    elif season == 'Winter':
        profit = km_per_season * 1.05
elif km_per_month <=10000:
    if season == 'Spring' or season == 'Autumn':
        profit = km_per_season * 0.95
    elif season == 'Summer':
        profit = km_per_season * 1.1
    elif season == 'Winter':
        profit = km_per_season * 1.25
elif km_per_month <=20000:
    profit = km_per_season * 1.45
profit -= profit * 0.1
print(f'{profit:.2f}')