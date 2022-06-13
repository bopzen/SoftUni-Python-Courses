budget = float(input())
season = input()
car_class = ''
car_type = ''
rent = 0
if budget <=100:
    car_class = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        rent = budget *0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        rent = budget * 0.65
elif budget <=500:
    car_class = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        rent = budget *0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        rent = budget * 0.80
elif budget >500:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    rent = budget * 0.9
print(f'{car_class}')
print(f'{car_type} - {rent:.2f}')