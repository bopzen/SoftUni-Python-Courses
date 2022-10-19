destination = input()
package = input()
is_vip = input()
days = int(input())
total = 0
price = 0
vip_discount = 0
if days > 7:
    days -= 1
if days >= 1:
    if destination == 'Bansko' or destination == 'Borovets':
        if package == 'withEquipment':
            price = 100
            if is_vip == 'yes':
                vip_discount = 0.1
            total = days * price
            total -= total * vip_discount
            print(f"The price is {total:.2f}lv! Have a nice time!")
        elif package == 'noEquipment':
            price = 80
            if is_vip == 'yes':
                vip_discount = 0.05
            total = days * price
            total -= total * vip_discount
            print(f"The price is {total:.2f}lv! Have a nice time!")
        else:
            print('Invalid input!')
    elif destination == 'Varna' or destination == 'Burgas':
        if package == 'withBreakfast':
            price = 130
            if is_vip == 'yes':
                vip_discount = 0.12
            total = days * price
            total -= total * vip_discount
            print(f"The price is {total:.2f}lv! Have a nice time!")
        elif package == 'noBreakfast':
            price = 100
            if is_vip == 'yes':
                vip_discount = 0.07
            total = days * price
            total -= total * vip_discount
            print(f"The price is {total:.2f}lv! Have a nice time!")
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
else:
    print("Days must be positive number!")