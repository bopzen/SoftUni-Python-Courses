import re

count = int(input())
attacked_planets = []
destroyed_planets = []
search_pattern = r"@([A-Za-z]+)[^@\-!:>]*?:([0-9]+)[^@\-!:>]*?!([A|D])![^@\-!:>]*?->[^@\-!:>]*?([0-9]+)"
for _ in range(count):
    encrypted_message = input()
    decrypted_message = ""
    key = 0
    for ch in encrypted_message:
        if ch.lower() in 'star':
            key += 1
    for ch in encrypted_message:
        decrypted_message += chr(ord(ch) - key)
    result = re.search(search_pattern, decrypted_message)
    if result:
        planet, population, attack_type, soldiers = result.groups()
        if attack_type == 'A':
            attacked_planets.append(planet)
        elif attack_type == 'D':
            destroyed_planets.append(planet)
print("Attacked planets:", end=" ")
if len(attacked_planets) > 0:
    print(len(attacked_planets))
    for element in sorted(attacked_planets):
        print(f"-> {element}")
else:
    print(0)
print("Destroyed planets:", end=" ")
if len(destroyed_planets) > 0:
    print(len(destroyed_planets))
    for element in sorted(destroyed_planets):
        print(f"-> {element}")
else:
    print(0)