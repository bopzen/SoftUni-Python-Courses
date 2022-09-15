from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(list(map(int, input().split())))
value_intelligence = int(input())
bullet_cost = 0
load = gun_barrel_size
while locks:
    if bullets:
        shot = bullets.pop()
        load -= 1
        bullet_cost += bullet_price
        if shot <= locks[0]:
            locks.popleft()
            print('Bang!')
        else:
            print('Ping!')
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    if load == 0 and bullets:
        print('Reloading!')
        load = gun_barrel_size
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value_intelligence-bullet_cost}")