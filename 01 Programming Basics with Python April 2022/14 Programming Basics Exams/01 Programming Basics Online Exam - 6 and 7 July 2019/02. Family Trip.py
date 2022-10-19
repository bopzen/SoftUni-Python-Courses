budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_expenses_percent = int(input())
discount = 0
additional_expenses = budget * additional_expenses_percent/100
total = nights * price_per_night
if nights > 7:
    discount = 0.05
total -= total*discount
total += additional_expenses
if budget >= total:
    money_left = budget - total
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    money_needed = total - budget
    print(f"{money_needed:.2f} leva needed.")
