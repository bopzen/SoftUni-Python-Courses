budget = int(input())
season = input()
fishermen = int(input())
boat_rent = 0
discount = 0
if season == 'Spring':
    boat_rent = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
elif season == 'Winter':
    boat_rent = 2600

if fishermen >=12:
    discount = 0.25
elif fishermen >=7:
    discount = 0.15
else:
    discount = 0.1
total_price = boat_rent - boat_rent*discount

if fishermen % 2 == 0 and season !='Autumn':
    total_price-=total_price*0.05

if budget >= total_price:
    money_left = budget - total_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")