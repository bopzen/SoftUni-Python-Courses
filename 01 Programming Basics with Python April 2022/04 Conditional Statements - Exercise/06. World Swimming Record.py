world_record = float(input())
distance = float(input())
speed = float(input())
slowing_down = distance//15*12.5
time = distance*speed + slowing_down
if time < world_record:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    print(f'No, he failed! He was {(time-world_record):.2f} seconds slower.')