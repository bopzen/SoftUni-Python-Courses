x = float(input())
y = float(input())
h = float(input())

area_walls = x * x * 2 - 1.2 * 2 + x * y * 2 - 1.5 * 1.5 *2
area_roof = x * y * 2 + x * h

amount_green = area_walls / 3.4
amount_red = area_roof / 4.3
print('{:.2f}'.format(amount_green))
print('{:.2f}'.format(amount_red))