cars_dict = {}
n = int(input())
for _ in range(n):
    command = input().split("|")
    car, mileage, fuel = command[0], int(command[1]), int(command[2])
    cars_dict[car] = {}
    cars_dict[car]['mileage'] = mileage
    cars_dict[car]['fuel'] = fuel

while True:
    command = input()
    if command == 'Stop':
        break
    tokens = command.split(" : ")
    action = tokens[0]
    if action == 'Drive':
        car, distance, fuel = tokens[1], int(tokens[2]), int(tokens[3])
        if fuel <= cars_dict[car]['fuel']:
            cars_dict[car]['fuel'] -= fuel
            cars_dict[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars_dict[car]['mileage'] >= 100000:
            del cars_dict[car]
            print(f"Time to sell the {car}!")
    elif action == 'Refuel':
        car, fuel = tokens[1], int(tokens[2])
        if cars_dict[car]['fuel'] + fuel > 75:
            refill = 75 - cars_dict[car]['fuel']
        else:
            refill = fuel
        cars_dict[car]['fuel'] += refill
        print(f"{car} refueled with {refill} liters")
    elif action == 'Revert':
        car, reversed_km = tokens[1], int(tokens[2])
        if cars_dict[car]['mileage'] - reversed_km <= 10000:
            cars_dict[car]['mileage'] = 10000
        else:
            cars_dict[car]['mileage'] -= reversed_km
            print(f"{car} mileage decreased by {reversed_km} kilometers")

for car in cars_dict:
    print(f"{car} -> Mileage: {cars_dict[car]['mileage']} kms, Fuel in the tank: {cars_dict[car]['fuel']} lt.")

