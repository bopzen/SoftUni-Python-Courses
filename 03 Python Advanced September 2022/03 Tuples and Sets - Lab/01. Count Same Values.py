numbers = tuple(map(float, input().split()))

unique = {}
for number in numbers:
    if number not in unique:
        unique[number] = 0
    unique[number] += 1

for number, count in unique.items():
    print(f"{number} - {count} times")