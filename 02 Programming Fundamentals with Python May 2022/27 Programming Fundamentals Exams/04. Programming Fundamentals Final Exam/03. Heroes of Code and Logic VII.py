n = int(input())
heroes_dict = {}

for _ in range(n):
    hero_stats = input().split()
    hero_name, hp, mp = hero_stats[0], int(hero_stats[1]), int(hero_stats[2])
    heroes_dict[hero_name] = {}
    heroes_dict[hero_name]['HP'] = min(hp, 100)
    heroes_dict[hero_name]['MP'] = min(mp, 200)

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split(" - ")
    action = tokens[0]
    if action == 'CastSpell':
        hero_name, mp_needed, spell_name = tokens[1], int(tokens[2]), tokens[3]
        if heroes_dict[hero_name]['MP'] >= mp_needed:
            heroes_dict[hero_name]['MP'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == 'TakeDamage':
        hero_name, damage, attacker = tokens[1], int(tokens[2]), tokens[3]
        heroes_dict[hero_name]['HP'] -= damage
        if heroes_dict[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['HP']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes_dict[hero_name]
    elif action == 'Recharge':
        hero_name, amount = tokens[1], int(tokens[2])
        if heroes_dict[hero_name]['MP'] + amount > 200:
            amount_recovered = 200 - heroes_dict[hero_name]['MP']
        else:
            amount_recovered = amount
        heroes_dict[hero_name]['MP'] += amount_recovered
        print(f"{hero_name} recharged for {amount_recovered} MP!")
    elif action == 'Heal':
        hero_name, amount = tokens[1], int(tokens[2])
        if heroes_dict[hero_name]['HP'] + amount > 100:
            amount_recovered = 100 - heroes_dict[hero_name]['HP']
        else:
            amount_recovered = amount
        heroes_dict[hero_name]['HP'] += amount_recovered
        print(f"{hero_name} healed for {amount_recovered} HP!")
for key, value in heroes_dict.items():
    print(key)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")

