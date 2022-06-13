list_sheeps = input().split(", ")
wolf_position = 0
for index, key in enumerate(list_sheeps):
    if key == 'wolf':
        wolf_position = index
if wolf_position == len(list_sheeps)-1:
    print("Please go away and stop eating my sheep")
else:
    element = ''
    counter = 0
    i = 1
    while list_sheeps[-i] != 'wolf':
        counter += 1
        i += 1
    print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")