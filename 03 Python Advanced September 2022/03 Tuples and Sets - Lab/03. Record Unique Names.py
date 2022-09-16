lines = int(input())
names = []
for _ in range(lines):
    names.append(input())
unique = set(names)
for name in unique:
    print(name)