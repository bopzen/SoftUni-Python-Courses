fruit = input()
pack_size = input()
count_packs = int(input())
price = 0
discount = 0
small = 2
big = 5
if pack_size == 'small':
    if fruit == 'Watermelon':
        price = count_packs * small * 56
    elif fruit == 'Mango':
        price = count_packs * small * 36.66
    elif fruit == 'Pineapple':
        price = count_packs * small * 42.10
    elif fruit == 'Raspberry':
        price = count_packs * small * 20
elif pack_size == 'big':
    if fruit == 'Watermelon':
        price = count_packs * big * 28.7
    elif fruit == 'Mango':
        price = count_packs * big * 19.6
    elif fruit == 'Pineapple':
        price = count_packs * big * 24.8
    elif fruit == 'Raspberry':
        price = count_packs * big * 15.2
if price >1000:
    discount = 0.5
elif price >=400:
    discount = 0.15
price -= price * discount
print(f'{price:.2f} lv.')