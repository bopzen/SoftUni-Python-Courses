product = input().lower()
town = input().lower()
quantity = float(input())
if town == 'sofia':
    if product == 'coffee':
        print(quantity*0.5)
    elif product == 'water':
        print(quantity*0.8)
    elif product == 'beer':
        print(quantity * 1.2)
    elif product == 'sweets':
        print(quantity * 1.45)
    elif product == 'peanuts':
        print(quantity * 1.6)
elif town == 'plovdiv':
    if product == 'coffee':
        print(quantity*0.4)
    elif product == 'water':
        print(quantity*0.7)
    elif product == 'beer':
        print(quantity * 1.15)
    elif product == 'sweets':
        print(quantity * 1.3)
    elif product == 'peanuts':
        print(quantity * 1.5)
elif town == 'varna':
    if product == 'coffee':
        print(quantity*0.45)
    elif product == 'water':
        print(quantity*0.7)
    elif product == 'beer':
        print(quantity * 1.1)
    elif product == 'sweets':
        print(quantity * 1.35)
    elif product == 'peanuts':
        print(quantity * 1.55)