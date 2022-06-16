wagons = int(input())
list_wagons = [0] * wagons

while True:
    command = input()
    if command == 'End':
        break

    list_command = command.split()
    action = list_command[0]
    if action == 'add':
        people = int(list_command[1])
        list_wagons[-1] += people
    elif action == 'insert':
        index = int(list_command[1])
        people = int(list_command[2])
        list_wagons[index] += people
    elif action == 'leave':
        index = int(list_command[1])
        people = int(list_command[2])
        list_wagons[index] -= people
print(list_wagons)