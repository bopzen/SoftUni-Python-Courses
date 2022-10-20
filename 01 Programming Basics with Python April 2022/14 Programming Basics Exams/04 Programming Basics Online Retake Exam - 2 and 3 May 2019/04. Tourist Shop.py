budget = float(input())
budget_left = budget
count_products = 0
total_cost = 0

while True:
    product_name = input()
    if product_name == 'Stop':
        print(f"You bought {count_products} products for {total_cost:.2f} leva.")
        break
    product_price = float(input())
    count_products += 1
    if count_products % 3 == 0:
        product_price /= 2
    if product_price > budget_left:
        print("You don't have enough money!")
        print(f"You need {product_price - budget_left:.2f} leva!")
        break
    total_cost += product_price
    budget_left -= product_price

