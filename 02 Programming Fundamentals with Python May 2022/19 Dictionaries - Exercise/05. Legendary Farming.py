materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
is_farmed = False
while True:
    command = input().split()
    for i in range(0, len(command), 2):
        quantity, material = int(command[i]), command[i+1].lower()
        if material not in materials_dict:
            materials_dict[material] = quantity
        else:
            materials_dict[material] += quantity
        if materials_dict['shards'] >= 250:
            print("Shadowmourne obtained!")
            materials_dict['shards'] -= 250
            is_farmed = True
            break
        elif materials_dict['fragments'] >= 250:
            print("Valanyr obtained!")
            materials_dict['fragments'] -= 250
            is_farmed = True
            break
        elif materials_dict['motes'] >= 250:
            print("Dragonwrath obtained!")
            materials_dict['motes'] -= 250
            is_farmed = True
            break
    if is_farmed:
        break

print("\n".join(f"{key}: {materials_dict[key]}" for key in ['shards', 'fragments', 'motes']))
print("\n".join(f"{key}: {value}" for key, value in materials_dict.items() if key not in ['shards', 'fragments', 'motes']))