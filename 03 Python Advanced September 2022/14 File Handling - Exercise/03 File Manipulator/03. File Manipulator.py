import os

command = input().split('-')

while command[0] != 'End':
    if command[0] == 'Create':
        file_name = command[1]
        file = open(file_name, 'w')
        file.close()
    elif command[0] == 'Add':
        file_name, content = command[1], command[2]
        file = open(file_name, 'a')
        file.write(f'{content}\n')
        file.close()
    elif command[0] == 'Replace':
        file_name, old_string, new_string = command[1], command[2], command[3]
        try:
            with open(file_name, 'r') as file:
                data = file.readlines()
                for i in range(len(data)):
                    data[i] = data[i].replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.writelines(data)
        except FileNotFoundError:
            print('An error occurred')
    elif command[0] == 'Delete':
        file_name = command[1]
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')

    command = input().split('-')