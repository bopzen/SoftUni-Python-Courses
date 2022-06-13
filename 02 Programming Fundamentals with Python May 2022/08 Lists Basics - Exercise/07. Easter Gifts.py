list_gifts = input().split()
command = input()
while command != 'No Money':
    list_command = command.split()
    if list_command[0] == 'OutOfStock':
        for index in range(len(list_gifts)):
            if list_gifts[index] == list_command[1]:
                list_gifts[index] = 'None'
    elif list_command[0] == 'Required':
        if len(list_gifts) > int(list_command[2]) > 0:
            list_gifts[int(list_command[2])] = list_command[1]
    elif list_command[0] == 'JustInCase':
        list_gifts[-1] = list_command[1]
    command = input()
for element in list_gifts:
    if element != 'None':
        print(element, end=' ')