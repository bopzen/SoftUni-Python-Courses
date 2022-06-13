import sys

min_number = sys.maxsize

while True:
    number = input()
    if number == 'Stop':
        break
    else:
        number = int(number)
        if number < min_number:
            min_number = number
print(min_number)