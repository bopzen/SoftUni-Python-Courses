budget = float(input())
liters = float(input())
weekday = input()
total_price = liters * 2.1 + 100
if weekday == 'Saturday':
    total_price -= total_price * 0.1
elif weekday == 'Sunday':
    total_price -= total_price * 0.2
if budget >= total_price:
    money_left = budget - total_price
    print(f"Safari time! Money left: {money_left:.2f} lv.")
else:
    money_needed = total_price - budget
    print(f"Not enough money! Money needed: {money_needed:.2f} lv.")