all_fires = input()
all_fires = all_fires.replace(' = ', '#')
all_fires = all_fires.split('#')
water = int(input())
effort = 0
total_fire = 0
print('Cells:')
for index in range(0, len(all_fires) - 1,2):
    if ((all_fires[index] == 'High' and 81 <= int(all_fires[index + 1]) <= 125) \
            or (all_fires[index] == 'Medium' and 51 <= int(all_fires[index + 1]) <= 80) \
            or (all_fires[index] == 'Low' and 1 <= int(all_fires[index + 1]) <= 50)) \
            and water >= int(all_fires[index + 1]):
        print(f" - {all_fires[index + 1]}")
        water -= int(all_fires[index + 1])
        effort += 0.25 * int(all_fires[index + 1])
        total_fire += int(all_fires[index + 1])
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")