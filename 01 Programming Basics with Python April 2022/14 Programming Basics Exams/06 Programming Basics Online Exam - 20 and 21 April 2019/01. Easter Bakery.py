price_flour = float(input())
kg_flour = float(input())
kg_sugar = float(input())
count_egg_carton = int(input())
packs_yeast = int(input())
price_sugar = price_flour - price_flour * 0.25
price_egg_carton = price_flour + price_flour * 0.1
price_pack_yeast = price_sugar - price_sugar * 0.8

total_cost = price_flour * kg_flour + price_sugar * kg_sugar + price_egg_carton * count_egg_carton + price_pack_yeast * packs_yeast
print(f'{total_cost:.2f}')