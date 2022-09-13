from collections import deque
queue = deque()
water_quantity = int(input())

while True:
    name = input()
    if name == 'Start':
        break
    queue.append(name)

while True:
    command = input()
    if command == 'End':
        break
    elif 'refill' in command:
        command = command.split()
        liters = int(command[1])
        water_quantity += liters
    else:
        liters = int(command)
        if water_quantity >= liters:
            print(f'{queue.popleft()} got water')
            water_quantity -= liters
        else:
            print(f'{queue.popleft()} must wait')
print(f'{water_quantity} liters left')