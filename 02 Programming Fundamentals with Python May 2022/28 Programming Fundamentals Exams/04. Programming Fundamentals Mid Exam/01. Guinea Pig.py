food_kg = float(input())*1000
hay_kg = float(input())*1000
cover_kg = float(input())*1000
pig_weight_kg = float(input())*1000
need_more_food =  False
for day in range(1, 31):
    food_kg -= 300
    if day % 2 == 0:
        hay_kg -= food_kg * 0.05
    if day % 3 == 0:
        cover_kg -= pig_weight_kg / 3
    if food_kg <= 0 or hay_kg <= 0 or cover_kg <= 0:
        need_more_food = True
        break
if need_more_food:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_kg/1000:.2f}, Hay: {hay_kg/1000:.2f}, Cover: {cover_kg/1000:.2f}.")