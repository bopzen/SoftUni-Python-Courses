import math
days = int(input())
food = float(input())
total_food = 0
total_dog_food = 0
total_cat_food = 0
biscuits = 0
for i in range(1,days+1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_food += dog_food
    total_cat_food += cat_food
    if i % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.10
total_biscuits = math.floor(biscuits)
total_food = total_dog_food + total_cat_food
print(f"Total eaten biscuits: {total_biscuits}gr.")
print(f"{total_food/food*100:.2f}% of the food has been eaten.")
print(f"{total_dog_food/total_food*100:.2f}% eaten from the dog.")
print(f"{total_cat_food/total_food*100:.2f}% eaten from the cat.")

