count_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
max_eggs = 0
max_eggs_color = ''
for i in range(count_eggs):
    color = input()
    if color == 'red':
        red +=1
    elif color == 'orange':
        orange +=1
    elif color == 'blue':
        blue +=1
    elif color == 'green':
        green +=1

if red > orange and red > blue and red > green:
    max_eggs = red
    max_eggs_color = 'red'
elif orange > red and orange > blue and orange > green:
    max_eggs = orange
    max_eggs_color = 'orange'
elif blue > red and blue > orange and blue > green:
    max_eggs = blue
    max_eggs_color = 'blue'
elif green > red and green > orange and green > blue:
    max_eggs = green
    max_eggs_color = 'green'

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_eggs_color}")
