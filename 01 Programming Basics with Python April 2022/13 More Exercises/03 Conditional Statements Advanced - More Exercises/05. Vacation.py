budget = float(input())
season = input()
location = ''
base = ''
if budget <= 1000:
    base = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif budget <= 3000:
    base = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60
elif budget > 3000:
    base = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.9
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.9
print(f'{location} - {base} - {price:.2f}')