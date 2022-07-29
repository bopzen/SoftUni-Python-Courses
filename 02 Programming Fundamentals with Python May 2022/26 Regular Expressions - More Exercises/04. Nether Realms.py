import re

demon_input = input()
search_demon_split_pattern = r"\s*,\s*|,\s*"
demon_names = re.split(search_demon_split_pattern, demon_input)

for i in range(len(demon_names)):
    demon_names[i] = demon_names[i].strip()

for demon in sorted(demon_names):
    search_pattern_health = r"[^0-9+\-\*/\.]"
    health_list = re.findall(search_pattern_health, demon)
    health = 0
    if health_list:
        for element in health_list:
            health += ord(element)
    search_pattern_damage = r"[+|-]?\d+\.?\d*"
    damage_list = re.findall(search_pattern_damage, demon)
    damage = 0
    if damage_list:
        for element in damage_list:
            damage += float(element)
    multiply = demon.count('*')
    divide = demon.count('/')
    if multiply != 0:
        damage *= 2 ** multiply
    if divide != 0:
        damage /= 2 ** divide
    print(f"{demon} - {health} health, {damage:.2f} damage")