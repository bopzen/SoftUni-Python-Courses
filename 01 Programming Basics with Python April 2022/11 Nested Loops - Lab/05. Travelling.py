saved = 0
while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    while saved < budget:
        amount = float(input())
        saved += amount
    saved = 0
    print(f'Going to {destination}!')