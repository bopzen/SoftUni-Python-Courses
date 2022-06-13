n = int(input())
capacity = 255
filled = 0
for i in range(n):
    liters = int(input())
    if liters > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= liters
        filled += liters
print(filled)