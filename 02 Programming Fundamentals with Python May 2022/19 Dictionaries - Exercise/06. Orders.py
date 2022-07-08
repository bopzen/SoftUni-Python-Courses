product_dict = {}
while True:
    command = input()
    if command == 'buy':
        break
    list_commands = command.split()
    name, price, quantity = list_commands[0], float(list_commands[1]), int(list_commands[2])
    if name not in product_dict:
        product_dict[name] = [price, quantity]
    else:
        product_dict[name][0] = price
        product_dict[name][1] += quantity

print("\n".join(f"{key} -> {product_dict[key][0] * product_dict[key][1]:.2f}" for key in product_dict.keys()))