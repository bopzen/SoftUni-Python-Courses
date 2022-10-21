cities = {}
while True:
    command = input()
    if command == 'Sail':
        break
    tokens = command.split("||")
    town, population, gold = tokens[0], int(tokens[1]), int(tokens[2])
    if town not in cities:
        cities[town] = {}
        cities[town]['Population'] = population
        cities[town]['Gold'] = gold
    else:
        cities[town]['Population'] += population
        cities[town]['Gold'] += gold

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split("=>")
    action = tokens[0]
    if action == 'Plunder':
        town, people, gold = tokens[1], int(tokens[2]), int(tokens[3])
        if people >= cities[town]['Population']:
            people_killed = cities[town]['Population']
        else:
            people_killed = people
        if gold >= cities[town]['Gold']:
            gold_stolen = cities[town]['Gold']
        else:
            gold_stolen = gold
        cities[town]['Population'] -= people_killed
        cities[town]['Gold'] -= gold_stolen
        print(f"{town} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.")
        if cities[town]['Population'] <= 0 or cities[town]['Gold'] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]
    elif action == 'Prosper':
        town, gold = tokens[1], int(tokens[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]['Gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['Gold']} gold.")
if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key in cities.keys():
        print(f"{key} -> Population: {cities[key]['Population']} citizens, Gold: {cities[key]['Gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

