number_of_orders = int(input())
total = 0
for i in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    price = price_capsule * days * capsules_per_day
    if 0.01 <= price_capsule <= 100000 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        print(f"The price for the coffee is: ${price:.2f}")
        total += price
print(f"Total: ${total:.2f}")