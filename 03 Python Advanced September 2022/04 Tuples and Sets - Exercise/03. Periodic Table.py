lines = int(input())
elements = set()
for _ in range(lines):
    command = input().split()
    for element in command:
        elements.add(element)
for element in elements:
    print(element)