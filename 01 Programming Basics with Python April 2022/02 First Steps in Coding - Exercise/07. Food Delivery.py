count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())

order = count_chicken_menu*10.35 + count_fish_menu*12.4 + count_vegetarian_menu*8.15
dessert = order*0.2
total = order + dessert + 2.5

print(total)