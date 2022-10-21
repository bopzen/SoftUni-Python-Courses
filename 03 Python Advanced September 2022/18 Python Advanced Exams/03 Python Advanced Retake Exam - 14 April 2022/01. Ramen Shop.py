from collections import deque

bowls = list(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))

while bowls and customers:
    if bowls[-1] > customers[0]:
        bowls[-1] -= customers[0]
        customers.popleft()
    elif bowls[-1] < customers[0]:
        customers[0] -= bowls[-1]
        bowls.pop()
    else:
        customers.popleft()
        bowls.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")