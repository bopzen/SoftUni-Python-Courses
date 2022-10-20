contract_duration = input()
contract_type = input()
mobile_internet = input()
months = int(input())
monthly_fee = 0
if contract_type == 'Small':
    if contract_duration == "one":
        monthly_fee = 9.98
    elif contract_duration == 'two':
        monthly_fee = 8.58
elif contract_type == 'Middle':
    if contract_duration == "one":
        monthly_fee = 18.99
    elif contract_duration == 'two':
        monthly_fee = 17.09
elif contract_type == 'Large':
    if contract_duration == "one":
        monthly_fee = 25.98
    elif contract_duration == 'two':
        monthly_fee = 23.59
elif contract_type == 'ExtraLarge':
    if contract_duration == "one":
        monthly_fee = 35.99
    elif contract_duration == 'two':
        monthly_fee = 31.79
if mobile_internet == 'yes':
    if monthly_fee <= 10:
        monthly_fee += 5.5
    elif monthly_fee <= 30:
        monthly_fee += 4.35
    else:
        monthly_fee += 3.85
if contract_duration == 'two':
    monthly_fee -= monthly_fee * 0.0375
total = months * monthly_fee
print(f'{total:.2f} lv.')

