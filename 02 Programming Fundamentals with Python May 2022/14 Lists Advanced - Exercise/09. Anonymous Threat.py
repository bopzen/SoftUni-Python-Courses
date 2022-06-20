list_data = input().split()

while True:
    command = input()
    if command == '3:1':
        break
    list_command = command.split()
    action = list_command[0]
    if action == 'merge':
        start_index = int(list_command[1])
        end_index = int(list_command[2])
        if start_index >= len(list_data)-1 or end_index <= 0:
            continue
        if start_index < 0:
            start_index = 0
        if end_index > len(list_data)-1:
            end_index = len(list_data)-1
        merged_string = "".join(list_data[start_index:end_index+1:1])
        list_data.insert(start_index, merged_string)
        del list_data[start_index + 1:end_index+2]
    elif action == 'divide':
        index = int(list_command[1])
        partitions = int(list_command[2])
        division_string = list_data[index]
        partitions_length = len(division_string) // partitions
        list_division_string = []
        counter = 0
        for i in range(0, len(division_string), partitions_length):
            counter += 1
            if counter == partitions:
                list_division_string.append(division_string[i:])
                break
            else:
                list_division_string.append(division_string[i:i + partitions_length])
        list_data.pop(index)
        list_data[index:index] = list_division_string
print(" ".join(list_data))