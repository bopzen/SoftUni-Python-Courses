def total_price(product, quantity):
    result = None
    if product == 'coffee':
        result = quantity * 1.5
    elif product == 'water':
        result = quantity * 1
    elif product == 'coke':
        result = quantity * 1.4
    elif product == 'snacks':
        result = quantity * 2
    print(f'{result:.2f}')

product = input()
quantity = int(input())
total_price(product,quantity)
