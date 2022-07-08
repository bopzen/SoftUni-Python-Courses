resources_dict = {}

while True:
    command1 = input()
    if command1 == 'stop':
        break
    command2 = input()
    resource = command1
    quantity = int(command2)
    if resource not in resources_dict:
        resources_dict[resource] = quantity
    else:
        resources_dict[resource] += quantity

print("\n".join(f"{key} -> {value}" for key, value in resources_dict.items()))