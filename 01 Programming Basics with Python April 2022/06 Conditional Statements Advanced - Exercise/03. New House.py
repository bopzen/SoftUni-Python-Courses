flower = input()
count = int(input())
budget = int(input())
price_per_flower = 0
discount = 0
markup = 0
if flower == 'Roses':
    price_per_flower = 5
    if count > 80:
        discount = 0.1
elif flower == 'Dahlias':
    price_per_flower = 3.8
    if count > 90:
        discount = 0.15
elif flower == 'Tulips':
    price_per_flower = 2.8
    if count >80:
        discount = 0.15
elif flower == "Narcissus":
    price_per_flower = 3
    if count <120:
        markup = 0.15
elif flower == 'Gladiolus':
    price_per_flower = 2.5
    if count < 80:
        markup = 0.2
total_price = price_per_flower * count
total_price -=total_price*discount
total_price +=total_price*markup
if budget >=total_price:
    money_left = budget - total_price
    print(f"Hey, you have a great garden with {count} {flower} and {money_left:.2f} leva left.")
else:
    money_needed = total_price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")