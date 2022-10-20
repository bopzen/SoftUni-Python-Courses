amount_food = int(input())
food_eaten = 0
portion = input()
while portion != 'Adopted':
    food_eaten += int(portion)
    portion = input()
if food_eaten <= amount_food * 1000:
    food_left = amount_food * 1000 - food_eaten
    print(f"Food is enough! Leftovers: {food_left} grams.")
else:
    food_needed = food_eaten - amount_food * 1000
    print(f"Food is not enough. You need {food_needed} grams more." )