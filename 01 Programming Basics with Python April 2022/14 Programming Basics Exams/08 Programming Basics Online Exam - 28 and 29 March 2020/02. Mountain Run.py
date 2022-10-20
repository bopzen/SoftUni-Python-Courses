record = float(input())
distance = float(input())
speed = float(input())
time = distance*speed+distance//50*30
if time<record:
    print(f'Yes! The new record is {time:.2f} seconds.')
else:
    diff = time - record
    print(f'No! He was {diff:.2f} seconds slower.')