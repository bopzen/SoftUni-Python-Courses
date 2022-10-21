n = int(input())
plants_dict = {}
for _ in range(n):
    command = input().split("<->")
    plant, rarity = command[0], int(command[1])
    plants_dict[plant] = {}
    plants_dict[plant]['rarity'] = rarity
    plants_dict[plant]['rating'] = []

while True:
    command = input()
    if command == 'Exhibition':
        break
    list_command = command.split(": ")
    action = list_command[0]
    plant_event = list_command[1]
    if action == "Rate":
        plant_event = plant_event.split(" - ")
        plant, rating = plant_event[0], int(plant_event[1])
        if plant in plants_dict:
            plants_dict[plant]['rating'].append(rating)
        else:
            print('error')
    elif action == 'Update':
        plant_event = plant_event.split(" - ")
        plant, new_rarity = plant_event[0], int(plant_event[1])
        if plant in plants_dict:
            plants_dict[plant]['rarity'] = new_rarity
        else:
            print('error')
    elif action == 'Reset':
        plant = plant_event
        if plant in plants_dict:
            plants_dict[plant]['rating'] = []
        else:
            print('error')

print("Plants for the exhibition:")
for key, value in plants_dict.items():
    if len(plants_dict[key]['rating']) > 0:
        average_rating = sum(plants_dict[key]['rating'])/len(plants_dict[key]['rating'])
    else:
        average_rating = 0
    print(f"- {key}; Rarity: {plants_dict[key]['rarity']}; Rating: {average_rating:.2f}")