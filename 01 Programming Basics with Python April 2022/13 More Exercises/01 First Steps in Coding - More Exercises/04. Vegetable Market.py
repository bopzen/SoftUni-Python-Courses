price_veggies = float(input())
price_fruits = float(input())
weight_kg_veggies = int(input())
weight_kg_fruits = int(input())

total_profit_EUR = (price_veggies * weight_kg_veggies + price_fruits * weight_kg_fruits) / 1.94
print('{:.2f}'.format(total_profit_EUR))