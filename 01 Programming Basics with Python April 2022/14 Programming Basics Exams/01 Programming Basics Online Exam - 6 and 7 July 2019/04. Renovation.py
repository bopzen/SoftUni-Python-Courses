import math

height = int(input())
width = int(input())
percent_area_no_paint = int(input())

area = height * width * 4
area = math.ceil(area - area * percent_area_no_paint/100)
area_left = area

while True:
    command = input()
    if command == 'Tired!':
        print(f"{area_left} quadratic m left." )
        break
    paint_liters = int(command)
    area_left -= paint_liters
    if area_left <=0:
        if area_left == 0:
            print("All walls are painted! Great job, Pesho!" )
        else:
            print(f"All walls are painted and you have {abs(area_left)} l paint left!")
        break