list_numbers = list(map(int,input().split()))

while True:
    command = input()
    if command == 'end':
        break
    list_command = command.split()
    if list_command[0] == 'swap':
        list_numbers[int(list_command[1])], list_numbers[int(list_command[2])] = list_numbers[int(list_command[2])], list_numbers[int(list_command[1])]
    elif list_command[0] == 'multiply':
        list_numbers[int(list_command[1])] *= list_numbers[int(list_command[2])]
    elif list_command[0] == 'decrease':
        for index in range(len(list_numbers)):
            list_numbers[index] -= 1
print(", ".join(list(map(str,list_numbers))))
