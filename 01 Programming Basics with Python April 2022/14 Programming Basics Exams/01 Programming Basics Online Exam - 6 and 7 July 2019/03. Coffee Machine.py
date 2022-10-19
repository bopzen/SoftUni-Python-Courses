drink = input()
sugar = input()
count_drinks = int(input())
price = 0
if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.9
    elif sugar == 'Normal':
        price = 1
    elif sugar == 'Extra':
        price = 1.2
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.2
    elif sugar == 'Extra':
        price = 1.6
elif drink == 'Tea':
    if sugar == 'Without':
        price = 0.5
    elif sugar == 'Normal':
        price = 0.6
    elif sugar == 'Extra':
        price = 0.7
total = count_drinks * price
if sugar == 'Without':
    total -= total * 0.35
if drink == 'Espresso' and count_drinks >=5:
    total -= total * 0.25
if total > 15:
    total -= total * 0.20
print(f"You bought {count_drinks} cups of {drink} for {total:.2f} lv.")