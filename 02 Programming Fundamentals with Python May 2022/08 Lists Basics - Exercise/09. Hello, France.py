list_items = input().split("|")
budget = float(input())
list_new_price = []
sum_items = 0
for item in list_items:
    item_info = item.split("->")
    item_type = item_info[0]
    item_price = float(item_info[1])
    if budget >= item_price:
        if (item_type == 'Clothes' and item_price <= 50) \
                or (item_type == 'Shoes' and item_price <= 35) \
                or (item_type == 'Accessories' and item_price <= 20.5):
            budget -= item_price
            sum_items += item_price
            list_new_price.append(item_price + item_price*0.4)
for element in list_new_price:
    print(f"{element:.2f}", end=' ')
print()
sum_revenue = sum(list_new_price)
profit = sum_revenue - sum_items
print(f"Profit: {profit:.2f}")
budget = budget + sum_revenue
if budget >= 150:
    print("Hello, France!" )
else:
    print("Not enough money.")