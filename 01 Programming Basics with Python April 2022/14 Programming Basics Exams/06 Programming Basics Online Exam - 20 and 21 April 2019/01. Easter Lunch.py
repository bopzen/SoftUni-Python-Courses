count_panetone = int(input())
count_egg_cartons = int(input())
kg_cookies = int(input())
total_cost = count_panetone * 3.2 + count_egg_cartons * 4.35 + kg_cookies * 5.4 + count_egg_cartons*12*0.15
print(f'{total_cost:.2f}')