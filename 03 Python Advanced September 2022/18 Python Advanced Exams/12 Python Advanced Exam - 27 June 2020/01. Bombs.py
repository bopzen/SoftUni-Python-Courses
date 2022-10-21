from collections import deque

bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = list(map(int, input().split(", ")))
success = False
bombs_dict = {
    'Datura Bombs': {'required': 40, 'created': 0},
    'Cherry Bombs': {'required': 60, 'created': 0},
    'Smoke Decoy Bombs': {'required': 120, 'created': 0}
}

while bomb_effects and bomb_casings:
    for bomb in bombs_dict.keys():
        if bombs_dict[bomb]['required'] == bomb_effects[0] + bomb_casings[-1]:
            bombs_dict[bomb]['created'] += 1
            bomb_effects.popleft()
            bomb_casings.pop()
            for bomb in bombs_dict.keys():
                if bombs_dict[bomb]['created'] < 3:
                    break
            else:
                success = True
                break
            break
    else:
        bomb_casings[-1] -= 5
    if success:
        break

if not success:
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print("Bene! You have successfully filled the bomb pouch!")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

bombs_dict_sorted = sorted(bombs_dict.items(), key=lambda x: x[0])

for key, value in bombs_dict_sorted:
    print(f"{key}: {bombs_dict[key]['created']}")
