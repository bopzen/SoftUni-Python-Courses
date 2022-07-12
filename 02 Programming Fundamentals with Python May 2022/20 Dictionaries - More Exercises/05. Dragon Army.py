n = int(input())
dragon_stats = {}
for _ in range(n):
    command = input().split()
    type, name, damage, health, armor = command[0], command[1], command[2], command[3], command[4]
    if damage == 'null':
        damage = 45
    if health == 'null':
        health = 250
    if armor == 'null':
        armor = 10
    if type not in dragon_stats:
        dragon_stats[type] = {}
        if name not in dragon_stats[type]:
            dragon_stats[type][name] = {}
            dragon_stats[type][name] = {'damage': int(damage), 'health': int(health), 'armor': int(armor)}
    else:
        dragon_stats[type][name] = {'damage': int(damage), 'health': int(health), 'armor': int(armor)}

for type, name in dragon_stats.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    for nested_key, nested_value in name.items():
        total_damage += dragon_stats[type][nested_key]['damage']
        total_health += dragon_stats[type][nested_key]['health']
        total_armor += dragon_stats[type][nested_key]['armor']
    average_damage = total_damage / len(dragon_stats[type])
    average_health = total_health / len(dragon_stats[type])
    average_armor = total_armor / len(dragon_stats[type])
    print(f"{type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for nested_key, nested_value in sorted(name.items()):
        print(f"-{nested_key} -> damage: {dragon_stats[type][nested_key]['damage']}, health: {dragon_stats[type][nested_key]['health']}, armor: {dragon_stats[type][nested_key]['armor']}")



