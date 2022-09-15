from collections import deque

green_light = int(input())
free_window = int(input())
remaining_green = green_light
remaining_free = free_window
cars_queue = deque()
passed_cars = 0
crash = False

while True:
    command = input()
    if command == 'END':
        break
    if command == 'green':
        if cars_queue:
            while remaining_green > 0 and cars_queue:
                car = cars_queue.popleft()
                passing_car = deque(car)
                while passing_car:
                    last_letter = passing_car.popleft()
                    remaining_green -= 1
                    if remaining_green == 0:
                        break
                if not passing_car:
                    passed_cars += 1
            if passing_car:
                passed_window = False
                while True:
                    if not passing_car:
                        passed_window = True
                        break
                    if remaining_free == 0 and passing_car:
                        last_letter = passing_car.popleft()
                        crash = True
                        break
                    last_letter = passing_car.popleft()
                    remaining_free -= 1
                if passed_window:
                    passed_cars += 1
    else:
        cars_queue.append(command)
    if crash:
        break
    remaining_free = free_window
    remaining_green = green_light
if crash:
    print('A crash happened!')
    print(f'{car} was hit at {last_letter}.')
else:
    print('Everyone is safe.')
    print(f'{passed_cars} total cars passed the crossroads.')