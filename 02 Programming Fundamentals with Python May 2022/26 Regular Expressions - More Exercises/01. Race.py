import re

list_participants = input().split(", ")
dict_participants = {}
for element in list_participants:
    dict_participants[element] = 0

search_name = r"[A-Za-z]"
search_distance = r"[0-9]"

while True:
    name = ""
    distance = 0
    command = input()
    if command == 'end of race':
        break
    list_name = re.findall(search_name, command)
    list_distance = re.findall(search_distance, command)
    for element in list_name:
        name += element
    for element in list_distance:
        distance += int(element)
    if name in dict_participants:
        dict_participants[name] += distance

count = 1
for key, value in sorted(dict_participants.items(), key=lambda x: -x[1]):
    if count == 1:
        place = "1st"
    elif count == 2:
        place = "2nd"
    elif count == 3:
        place = "3rd"
    else:
        break
    print(f"{place} place: {key}")
    count += 1
