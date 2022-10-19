budget = float(input())
destination = input()
season = input()
days = int(input())
cost = 0
if destination == 'Dubai':
    if season == 'Winter':
        cost = days * 45000
    elif season == 'Summer':
        cost = days * 40000
if destination == 'Sofia':
    if season == 'Winter':
        cost = days * 17000
    elif season == 'Summer':
        cost = days * 12500
if destination == 'London':
    if season == 'Winter':
        cost = days * 24000
    elif season == 'Summer':
        cost = days * 20250

if destination == 'Dubai':
    cost -= cost * 0.3
if destination == 'Sofia':
    cost += cost * 0.25

if budget >= cost:
    money_left = budget - cost
    print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")
else:
    money_needed = cost - budget
    print(f"The director needs {money_needed:.2f} leva more!")
