from collections import deque
quantity = int(input())
orders = list(map(int, input().split()))
queue = deque(orders)
print(max(orders))

while len(queue):
    if quantity >= queue[0]:
        quantity -= queue.popleft()
    else:
        break
if len(queue):
    print('Orders left: ' + ' '.join(map(str, queue)))
else:
    print('Orders complete')