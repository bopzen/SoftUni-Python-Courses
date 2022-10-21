from collections import deque


def check_sum(curr_sum):
    if 100 <= curr_sum <= 199:
        gifts['Gemstone'] += 1
    elif 200 <= curr_sum <= 299:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= curr_sum <= 399:
        gifts['Gold'] += 1
    elif 400 <= curr_sum <= 499:
        gifts['Diamond Jewellery'] += 1


gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

while materials and magic_level:
    current_materials = materials.pop()
    current_magic_level = magic_level.popleft()
    current_sum = current_materials + current_magic_level
    if current_sum < 100:
        if current_sum % 2 == 0:
            current_sum = current_materials * 2 + current_magic_level * 3
        else:
            current_sum *= 2
        check_sum(current_sum)
    elif current_sum > 499:
        current_sum /= 2
        check_sum(current_sum)
    else:
        check_sum(current_sum)

if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or (gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")


for present, amount in sorted(gifts.items()):
    if amount > 0:
        print(f"{present}: {amount}")