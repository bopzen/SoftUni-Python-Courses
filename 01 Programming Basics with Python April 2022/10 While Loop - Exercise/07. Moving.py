width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height

while free_space >0:
    count_packages = input()
    if count_packages == 'Done':
        print(f"{free_space} Cubic meters left.")
        break
    count_packages = int(count_packages)
    free_space -= count_packages
if free_space <= 0:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")