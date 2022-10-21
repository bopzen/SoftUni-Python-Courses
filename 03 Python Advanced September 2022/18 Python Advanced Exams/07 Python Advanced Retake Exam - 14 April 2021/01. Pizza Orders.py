from collections import deque

pizza_orders = deque(map(int,input().split(", ")))
employees = list(map(int,input().split(", ")))
total_pizza = 0

while pizza_orders and employees:
    if pizza_orders[0] <= 0 or pizza_orders[0] > 10:
        pizza_orders.popleft()
    else:
        if employees[-1] >= pizza_orders[0]:
            total_pizza += pizza_orders.popleft()
            employees.pop()
        else:
            total_pizza += employees[-1]
            pizza_orders[0] -= employees[-1]
            employees.pop()

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")

