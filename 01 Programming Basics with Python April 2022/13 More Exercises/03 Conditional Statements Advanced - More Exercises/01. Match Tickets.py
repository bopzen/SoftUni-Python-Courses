budget = float(input())
category = input()
num_people = int(input())
transport = 0
if num_people >=1 and num_people <=4:
    transport = budget * 0.75
elif num_people >=5 and num_people <=9:
    transport = budget * 0.6
elif num_people >=10 and num_people <=24:
    transport = budget * 0.5
elif num_people >=25 and num_people <=49:
    transport = budget * 0.4
elif num_people >=50:
    transport = budget * 0.25
money_left = budget - transport
money_needed = 0
if category == 'VIP':
    money_needed = num_people * 499.99
elif category == 'Normal':
    money_needed = num_people * 249.99
if money_left >= money_needed:
    print(f'Yes! You have {money_left-money_needed:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_needed-money_left:.2f} leva.')