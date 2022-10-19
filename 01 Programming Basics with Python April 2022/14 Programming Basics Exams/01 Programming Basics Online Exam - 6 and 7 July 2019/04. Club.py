target_profit = float(input())
total_profit = 0

while True:
    cocktail_name = input()
    if cocktail_name == 'Party!':
        print(f"We need {target_profit-total_profit:.2f} leva more.")
        break
    count_cocktail = int(input())
    price_cocktail = len(cocktail_name)
    order_price = price_cocktail * count_cocktail
    if order_price % 2 !=0:
        order_price -= order_price * 0.25
    total_profit += order_price
    if total_profit >= target_profit:
        print('Target acquired.')
        break
print(f"Club income - {total_profit:.2f} leva.")