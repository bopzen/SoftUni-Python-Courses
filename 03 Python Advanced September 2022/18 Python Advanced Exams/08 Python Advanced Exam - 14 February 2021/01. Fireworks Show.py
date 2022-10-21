from collections import deque

fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}
success = False
firework_effects = deque(map(int, input().split(", ")))
explosive_power = list(map(int, input().split(", ")))

while firework_effects and explosive_power:
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    sum_mix = firework_effects[0] + explosive_power[-1]
    if sum_mix % 3 == 0 and sum_mix % 5 != 0:
        fireworks['Palm Fireworks'] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_mix % 5 == 0 and sum_mix % 3 != 0:
        fireworks['Willow Fireworks'] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_mix % 3 == 0 and sum_mix % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1
        firework_effects.append(firework_effects.popleft())

    if fireworks['Palm Fireworks'] >=3 and fireworks['Willow Fireworks'] >=3 and fireworks['Crossette Fireworks'] >=3:
        success = True
        break

if success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")
print('\n'.join(f"{key}: {value}" for key, value in fireworks.items()))