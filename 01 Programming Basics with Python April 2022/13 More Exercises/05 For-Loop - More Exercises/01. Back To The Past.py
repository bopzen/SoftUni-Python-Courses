money = float(input())
year = int(input())
expenses = 0
age = 18
for i in range(1800,year+1):
    if i % 2 == 0:
        expenses += 12000
    else:
        expenses += 12000 +50*age
    age+=1
if money >= expenses:
    money_left = money - expenses
    print(f'Yes! He will live a carefree life and will have {money_left:.2f} dollars left.')
else:
    money_needed = expenses - money
    print(f'He will need {money_needed:.2f} dollars to survive.')