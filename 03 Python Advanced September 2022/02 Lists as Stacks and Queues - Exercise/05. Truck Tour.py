from collections import deque

count_pumps = int(input())
pumps = deque()
is_complete = False
for _ in range(count_pumps):
    pumps.append(input())
index_pump = 0
for _ in range(count_pumps):
    tank = 0
    is_complete = True
    for pump in pumps:
        fill, distance = list(map(int,pump.split()))
        tank += fill
        if tank < distance:
            is_complete = False
            break
        tank -= distance
    if is_complete:
        print(index_pump)
        break
    index_pump += 1
    pumps.append(pumps.popleft())