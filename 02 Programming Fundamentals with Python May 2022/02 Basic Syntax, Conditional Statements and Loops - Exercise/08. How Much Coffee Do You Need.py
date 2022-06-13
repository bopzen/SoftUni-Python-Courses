count_coffee = 0
while True:
    event = input()
    if event == 'END':
        break
    if event == 'coding' or event == 'dog' or event == 'cat' or event == 'movie':
        count_coffee +=1
    elif event == 'CODING' or event == 'DOG' or event == 'CAT' or event == 'MOVIE':
        count_coffee += 2
    else:
        continue
if count_coffee > 5:
    print("You need extra sleep")
else:
    print(count_coffee)