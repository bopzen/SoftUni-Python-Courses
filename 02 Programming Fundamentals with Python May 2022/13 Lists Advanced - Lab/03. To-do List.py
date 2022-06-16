list_tasks = [0] * 10
while True:
    command = input()
    if command == 'End':
        break
    list_command = command.split("-")
    priority = int(list_command[0])-1
    task = list_command[1]
    list_tasks.pop(priority)
    list_tasks.insert(priority, task)
result = [element for element in list_tasks if element != 0]
print(result)