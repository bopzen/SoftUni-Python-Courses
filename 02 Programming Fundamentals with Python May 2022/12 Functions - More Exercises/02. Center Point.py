import math

def closest_point(x1, y1, x2, y2):
    distance1 = math.sqrt(x1**2 + y1**2)
    distance2 = math.sqrt(x2**2 + y2**2)
    if distance1 <= distance2:
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")


closest_point(float(input()), float(input()), float(input()), float(input()))