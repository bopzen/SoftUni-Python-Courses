list_events = input().split("|")
coins = 100
energy = 100
is_closed = False
for event in list_events:
    event_info = event.split("-")
    event_type = event_info[0]
    event_amount = int(event_info[1])
    if event_type == 'rest':
        temporary_energy = energy
        energy += event_amount
        if energy > 100:
            energy = 100
        gained_energy = energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_type == 'order':
        if energy >= 30:
            energy -= 30
            coins += event_amount
            print(f"You earned {event_amount} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")
    else:
        if coins >= event_amount:
            coins -= event_amount
            print(f"You bought {event_type}.")
        else:
            is_closed = True
            print(f"Closed! Cannot afford {event_type}.")
            break
if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")