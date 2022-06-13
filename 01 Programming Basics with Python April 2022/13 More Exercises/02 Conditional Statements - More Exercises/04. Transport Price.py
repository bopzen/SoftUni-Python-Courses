distance = int(input())
part_of_day = input()
taxi_day = distance * 0.79 + 0.70
taxi_night = distance * 0.90 + 0.70
bus = distance * 0.09
train = distance * 0.06
cheapest = 0
if distance >=100 and part_of_day =='day':
    cheapest = min(taxi_day,bus,train)
elif distance >=20 and part_of_day =='day':
    cheapest = min(taxi_day,bus)
elif distance <20 and part_of_day == 'day':
    cheapest = taxi_day
if distance >=100 and part_of_day =='night':
    cheapest = min(taxi_night,bus,train)
elif distance >=20 and part_of_day =='night':
    cheapest = min(taxi_night,bus)
elif distance <20 and part_of_day == 'night':
    cheapest = taxi_night
print(f'{cheapest:.2f}')