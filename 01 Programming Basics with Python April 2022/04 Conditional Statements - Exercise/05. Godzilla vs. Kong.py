budget = float(input())
count_statists = int(input())
price_clothing = float(input())
price_decor = budget*0.1
if count_statists > 150:
    expenses_statists = count_statists*price_clothing-count_statists*price_clothing*0.1
else:
    expenses_statists = count_statists*price_clothing
total_expenses = price_decor + expenses_statists
if budget >= total_expenses:
    print('Action!')
    print(f'Wingard starts filming with {(budget-total_expenses):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {(total_expenses-budget):.2f} leva more.')