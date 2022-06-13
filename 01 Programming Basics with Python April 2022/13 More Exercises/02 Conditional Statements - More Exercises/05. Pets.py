import math

days = int(input())
food = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_g = float(input())
dog = days*dog_food_per_day_kg
cat = days*cat_food_per_day_kg
turtle = days*turtle_food_per_day_g/1000
total = dog + cat + turtle
if total <=food:
    left=math.floor(food-total)
    print(f'{left} kilos of food left.')
else:
    left = math.ceil(total - food)
    print(f'{left} more kilos of food are needed.')