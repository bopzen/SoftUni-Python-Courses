capacity = float(input())
filled_capacity = 0
left_capacity = capacity
counter = 1
counter_luggage = 0
while filled_capacity <= capacity:
    luggage_volume = input()
    if luggage_volume == 'End':
        print("Congratulations! All suitcases are loaded!")
        break
    luggage_volume = float(luggage_volume)
    if counter % 3 == 0:
        luggage_volume += luggage_volume * 0.1
    if luggage_volume <= left_capacity:
        filled_capacity += luggage_volume
        left_capacity = capacity - filled_capacity
        counter_luggage += 1
    else:
        print("No more space!")
        break
    counter += 1
print(f"Statistic: {counter_luggage} suitcases loaded.")

