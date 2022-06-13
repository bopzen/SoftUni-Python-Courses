city = input()
volume = float(input())
tier1 = volume >=0 and volume <=500
tier2 = volume >500 and volume <=1000
tier3 = volume >1000 and volume <=10000
tier4 = volume >10000
if tier1:
    if city == 'Sofia':
        commission = volume * 5/100
        print(f'{commission:.2f}')
    elif city == 'Varna':
        commission = volume * 4.5/100
        print(f'{commission:.2f}')
    elif city == 'Plovdiv':
        commission = volume * 5.5/100
        print(f'{commission:.2f}')
    else:
        print('error')
elif tier2:
    if city == 'Sofia':
        commission = volume * 7/100
        print(f'{commission:.2f}')
    elif city == 'Varna':
        commission = volume * 7.5/100
        print(f'{commission:.2f}')
    elif city == 'Plovdiv':
        commission = volume * 8/100
        print(f'{commission:.2f}')
    else:
        print('error')
elif tier3:
    if city == 'Sofia':
        commission = volume * 8/100
        print(f'{commission:.2f}')
    elif city == 'Varna':
        commission = volume * 10/100
        print(f'{commission:.2f}')
    elif city == 'Plovdiv':
        commission = volume * 12/100
        print(f'{commission:.2f}')
    else:
        print('error')
elif tier4:
    if city == 'Sofia':
        commission = volume * 12/100
        print(f'{commission:.2f}')
    elif city == 'Varna':
        commission = volume * 13/100
        print(f'{commission:.2f}')
    elif city == 'Plovdiv':
        commission = volume * 14.5/100
        print(f'{commission:.2f}')
    else:
        print('error')
else:
    print('error')