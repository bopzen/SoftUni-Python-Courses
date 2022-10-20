count_frame = int(input())
type_frame = input()
delivery = input()
price = 0
if count_frame < 10:
    print('Invalid order')
else:
    if type_frame == '90X130':
        if count_frame >=60:
            price = count_frame * 110
            price -= price *0.08
        elif count_frame >=30:
            price = count_frame * 110
            price -= price * 0.05
        else:
            price = count_frame * 110
    if type_frame == '100X150':
        if count_frame >=80:
            price = count_frame * 140
            price -= price * 0.1
        elif count_frame >=40:
            price = count_frame * 140
            price -= price * 0.06
        else:
            price = count_frame * 140
    if type_frame == '130X180':
        if count_frame >=50:
            price = count_frame * 190
            price -= price * 0.12
        elif count_frame >=20:
            price = count_frame * 190
            price -= price * 0.07
        else:
            price = count_frame * 190
    if type_frame == '200X300':
        if count_frame >=50:
            price = count_frame * 250
            price -= price * 0.14
        elif count_frame >=25:
            price = count_frame * 250
            price -= price * 0.09
        else:
            price = count_frame * 250
    if delivery == 'With delivery':
        price+= 60
    if count_frame > 99:
        price -= price *0.04
    print(f'{price:.2f} BGN')