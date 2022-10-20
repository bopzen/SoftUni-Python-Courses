egg_size = input()
egg_color = input()
egg_packs = int(input())
income = 0
if egg_size == 'Large':
    if egg_color == 'Red':
        income = egg_packs * 16
    elif egg_color == 'Green':
        income = egg_packs * 12
    elif egg_color == 'Yellow':
        income = egg_packs * 9
elif egg_size == 'Medium':
    if egg_color == 'Red':
        income = egg_packs * 13
    elif egg_color == 'Green':
        income = egg_packs * 9
    elif egg_color == 'Yellow':
        income = egg_packs * 7
elif egg_size == 'Small':
    if egg_color == 'Red':
        income = egg_packs * 9
    elif egg_color == 'Green':
        income = egg_packs * 8
    elif egg_color == 'Yellow':
        income = egg_packs * 5
profit = income - income * 0.35
print(f'{profit:.2f} leva.')