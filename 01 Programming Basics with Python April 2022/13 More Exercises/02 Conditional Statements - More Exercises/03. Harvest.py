import math
area = int(input())
grape_per_sq_m = float(input())
wine_liters = int(input())
workers = int(input())
total_grape = area * grape_per_sq_m
wine_grape = total_grape * 0.4
wine_production = wine_grape / 2.5
if wine_production < wine_liters:
    print(f'It will be a tough winter! More {math.floor(wine_liters-wine_production)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(wine_production)} liters.')
    print(f'{math.ceil(wine_production-wine_liters)} liters left -> {math.ceil((wine_production-wine_liters)/workers)} liters per person.')