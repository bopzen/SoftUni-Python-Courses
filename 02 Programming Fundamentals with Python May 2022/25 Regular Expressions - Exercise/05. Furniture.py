import re
total_cost = 0
bought_furniture = []
search_pattern = r">>([A-z]+)<<(\d+\.?\d+)!(\d+)"

while True:
    command = input()
    if command == 'Purchase':
        break
    result = re.search(search_pattern, command)
    if result:
        furniture, price, quantity = result.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)

print("Bought furniture:")
for element in bought_furniture:
    print(element)
print(f"Total money spend: {total_cost:.2f}")
