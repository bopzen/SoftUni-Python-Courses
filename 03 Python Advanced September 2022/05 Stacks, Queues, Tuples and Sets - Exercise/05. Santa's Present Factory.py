from collections import deque

materials = list(map(int, input().split()))
magic_values = deque(map(int, input().split()))

toys = {
    "Doll": {
        "magic": 150,
        "crafted": 0
    },
    "Wooden train": {
        "magic": 250,
        "crafted": 0
    },
    "Teddy bear":{
        "magic": 300,
        "crafted": 0
    },
    "Bicycle":{
        "magic": 400,
        "crafted": 0
    }
}

while materials and magic_values:
    flag = False
    if materials[-1] == 0:
        materials.pop()
        flag = True
    if magic_values[0] == 0:
        magic_values.popleft()
        flag = True
    if flag:
        continue

    total_magic_level = materials[-1] * magic_values[0]
    if total_magic_level == toys['Doll']['magic']:
        toys['Doll']['crafted'] += 1
        materials.pop()
        magic_values.popleft()
    elif total_magic_level == toys['Wooden train']['magic']:
        toys['Wooden train']['crafted'] += 1
        materials.pop()
        magic_values.popleft()
    elif total_magic_level == toys['Teddy bear']['magic']:
        toys['Teddy bear']['crafted'] += 1
        materials.pop()
        magic_values.popleft()
    elif total_magic_level == toys['Bicycle']['magic']:
        toys['Bicycle']['crafted'] += 1
        materials.pop()
        magic_values.popleft()
    elif total_magic_level < 0:
        materials.append(materials.pop() + magic_values.popleft())
    elif total_magic_level > 0:
        magic_values.popleft()
        materials[-1] += 15

if toys['Doll']['crafted'] > 0 and toys['Wooden train']['crafted'] >0 or toys['Teddy bear']['crafted'] > 0 and toys['Bicycle']['crafted'] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(materials[x]) for x in range(len(materials)-1,-1,-1))}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")
for toy in sorted(toys):
    if toys[toy]['crafted'] > 0:
        print(f"{toy}: {toys[toy]['crafted']}")