from collections import deque

customers = deque(map(int, input().split(", ")))
taxis = list(map(int, input().split(", ")))
total_time = 0

while customers and taxis:
    if taxis[-1] >= customers[0]:
        total_time += customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
