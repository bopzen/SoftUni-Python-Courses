count_guests = int(input())
price_per_guest = float(input())
budget = float(input())
discount = 0
price_cake = budget * 0.1
total_cost = count_guests * price_per_guest
if count_guests >20:
    discount = 0.25
elif count_guests >15:
    discount = 0.2
elif count_guests >=10:
    discount = 0.15
total_cost -= total_cost*discount
total_cost +=price_cake
if budget >= total_cost:
    money_left = budget - total_cost
    print(f"It is party time! {money_left:.2f} leva left.")
else:
    money_needed = total_cost - budget
    print(f"No party! {money_needed:.2f} leva needed.")