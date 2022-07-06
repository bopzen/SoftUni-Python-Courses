bakery = {}

while True:
    command = input()
    if command == 'statistics':
        break
    list_product = command.split(": ")
    product = list_product[0]
    quantity = int(list_product[1])
    if product in bakery:
        bakery[product] += quantity
    else:
        bakery[product] = quantity

print("Products in stock:")
for key, value in bakery.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")