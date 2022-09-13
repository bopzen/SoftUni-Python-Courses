from collections import deque

names = input().split()
toss = int(input())
players = deque(names)
i = 1
while len(players) > 1:
    kid = players.popleft()
    if i == toss:
        i = 0
        print(f'Removed {kid}')
    else:
        players.append(kid)
    i += 1

print(f'Last is {players.popleft()}')