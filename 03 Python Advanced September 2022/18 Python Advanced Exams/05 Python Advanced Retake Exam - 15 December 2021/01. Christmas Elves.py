from collections import deque

elves_energy = deque(map(int, input().split()))
material_boxes = list(map(int, input().split()))

total_used_energy = 0
total_toys = 0
turns = 0
while elves_energy and material_boxes:
    turns += 1
    current_elf_energy = elves_energy.popleft()
    if current_elf_energy < 5:
        continue
    energy_needed = material_boxes[-1]
    toys = 1
    if turns % 3 == 0:
        energy_needed *= 2
        toys = 2
    if current_elf_energy < energy_needed:
        if turns % 5 == 0:
            material_boxes.pop()
            total_used_energy += current_elf_energy
            current_elf_energy = 0
        else:
            current_elf_energy *= 2
        toys = 0
        elves_energy.append(current_elf_energy)
    else:
        current_elf_energy -= energy_needed
        total_used_energy += energy_needed
        material_boxes.pop()
        if turns % 5 == 0:
            toys = 0
        else:
            current_elf_energy += 1
        elves_energy.append(current_elf_energy)
        total_toys += toys


print(f"Toys: {total_toys}")
print(f"Energy: {total_used_energy}")
if elves_energy:
    print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")
if material_boxes:
    print(f"Boxes left: {', '.join([str(x) for x in material_boxes])}")
