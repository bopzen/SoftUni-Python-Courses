try:
    file = open('./numbers.txt', 'r')
    total = 0
    for line in file:
        total += int(line)
    file.close()
    print(total)
except FileNotFoundError:
    print('File not found')