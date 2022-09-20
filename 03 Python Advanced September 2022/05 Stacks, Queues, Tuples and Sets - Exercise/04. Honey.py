from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    if bees[0] <= nectar[-1]:
        collected_nectar, bee = nectar.pop(), bees.popleft()
        symbol = symbols.popleft()
        if symbol == "+":
            total_honey += abs(bee + collected_nectar)
        elif symbol == "-":
            total_honey += abs(bee - collected_nectar)
        elif symbol == "*":
            total_honey += abs(bee * collected_nectar)
        elif symbol == "/":
            if collected_nectar == 0 or bee == 0:
                continue
            else:
                total_honey += abs(bee / collected_nectar)
    else:
        nectar.pop()
print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")