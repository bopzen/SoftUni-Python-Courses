import re
total = 0
search_pattern = r"%([A-Z][a-z]*)%[^\|\$\.%]*?<(\w+)>[^\|\$\.%]*?\|(\d+)\|[^\|\$\.]*?([0-9]+(\.[0-9]+)?)\$"

while True:
    command = input()
    if command == 'end of shift':
        break
    result = re.search(search_pattern, command)
    if result:
        customer_name = result.group(1)
        product = result.group(2)
        quantity = int(result.group(3))
        price = float(result.group(4))
        total += quantity * price
        print(f"{customer_name}: {product} - {quantity * price:.2f}")

print(f"Total income: {total:.2f}")
