import math
magnolia = int(input())
ziumbiul = int(input())
rozi = int(input())
kaktusi = int(input())
gift = float(input())
sale = magnolia*3.25 + ziumbiul*4 + rozi*3.5 + kaktusi*8
sale-=sale*0.05
if sale >= gift:
    left = math.floor(sale-gift)
    print(f'She is left with {left} leva.')
else:
    left = math.ceil(gift-sale)
    print(f'She will have to borrow {left} leva.')