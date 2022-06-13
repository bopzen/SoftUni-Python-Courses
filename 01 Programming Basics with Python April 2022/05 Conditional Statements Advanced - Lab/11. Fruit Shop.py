fruit = input()
weekday = input()
amount = float(input())
intraweek = weekday == 'Monday' or weekday == 'Tuesday' or weekday == 'Wednesday' or weekday == 'Thursday' or weekday == 'Friday'
weekend = weekday == 'Saturday' or weekday == 'Sunday'
if intraweek:
    if fruit == 'banana':
        total = amount * 2.5
        print(f'{total:.2f}')
    elif fruit == 'apple':
        total = amount * 1.2
        print(f'{total:.2f}')
    elif fruit == 'orange':
        total = amount * 0.85
        print(f'{total:.2f}')
    elif fruit == 'grapefruit':
        total = amount * 1.45
        print(f'{total:.2f}')
    elif fruit == 'kiwi':
        total = amount * 2.7
        print(f'{total:.2f}')
    elif fruit == 'pineapple':
        total = amount * 5.5
        print(f'{total:.2f}')
    elif fruit == 'grapes':
        total = amount * 3.85
        print(f'{total:.2f}')
    else:
        print('error')
elif weekend:
    if fruit == 'banana':
        total = amount * 2.7
        print(f'{total:.2f}')
    elif fruit == 'apple':
        total = amount * 1.25
        print(f'{total:.2f}')
    elif fruit == 'orange':
        total = amount * 0.9
        print(f'{total:.2f}')
    elif fruit == 'grapefruit':
        total = amount * 1.6
        print(f'{total:.2f}')
    elif fruit == 'kiwi':
        total = amount * 3
        print(f'{total:.2f}')
    elif fruit == 'pineapple':
        total = amount * 5.6
        print(f'{total:.2f}')
    elif fruit == 'grapes':
        total = amount * 4.2
        print(f'{total:.2f}')
    else:
        print('error')
else:
    print('error')