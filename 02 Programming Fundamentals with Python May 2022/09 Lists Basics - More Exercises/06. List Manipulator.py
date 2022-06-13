list_numbers_str = input().split()
list_numbers = []
for element in list_numbers_str:
    list_numbers.append(int(element))
command = input()

while command != 'end':
    list_command = command.split()
    operation = list_command[0]

    if operation == 'exchange':
        index = int(list_command[1])
        if 0 <= index <= len(list_numbers) - 1:
            exchange_list = []
            for i in range(index+1, len(list_numbers)):
                exchange_list.append(list_numbers[i])
            for i in range(index+1):
                exchange_list.append(list_numbers[i])
            list_numbers = exchange_list
        else:
            print('Invalid index')

    elif operation == 'max':
        number_type = list_command[1]
        if number_type == 'odd':
            max_odd = -1
            max_odd_index = 0
            for index in range(len(list_numbers)):
                if list_numbers[index] % 2 != 0 and list_numbers[index] >= max_odd:
                    max_odd = list_numbers[index]
                    max_odd_index = index
            if max_odd == -1:
                print('No matches')
            else:
                print(max_odd_index)
        if number_type == 'even':
            max_even = -1
            max_even_index = 0
            for index in range(len(list_numbers)):
                if list_numbers[index] % 2 == 0 and list_numbers[index] >= max_even:
                    max_even = list_numbers[index]
                    max_even_index = index
            if max_even == -1:
                print('No matches')
            else:
                print(max_even_index)

    elif operation == 'min':
        number_type = list_command[1]
        if number_type == 'odd':
            min_odd = 1001
            min_odd_index = 0
            for index in range(len(list_numbers)):
                if list_numbers[index] % 2 != 0 and list_numbers[index] <= min_odd:
                    min_odd = list_numbers[index]
                    min_odd_index = index
            if min_odd == 1001:
                print('No matches')
            else:
                print(min_odd_index)
        if number_type == 'even':
            min_even = 1001
            min_even_index = 0
            for index in range(len(list_numbers)):
                if list_numbers[index] % 2 == 0 and list_numbers[index] <= min_even:
                    min_even = list_numbers[index]
                    min_even_index = index
            if min_even == 1001:
                print('No matches')
            else:
                print(min_even_index)

    elif operation == 'first':
        count = int(list_command[1])
        number_type = list_command[2]
        if count > len(list_numbers):
            print('Invalid count')
        else:
            counter = 0
            list_odd_numbers = []
            list_even_numbers = []
            if number_type == 'odd':
                for element in list_numbers:
                    if element % 2 != 0:
                        list_odd_numbers.append(element)
                        counter += 1
                        if counter == count:
                            break
                print(list_odd_numbers)
            elif number_type == 'even':
                for element in list_numbers:
                    if element % 2 == 0:
                        list_even_numbers.append(element)
                        counter += 1
                        if counter == count:
                            break
                print(list_even_numbers)
    elif operation == 'last':
        count = int(list_command[1])
        number_type = list_command[2]
        if count > len(list_numbers):
            print('Invalid count')
        else:
            counter = 0
            list_odd_numbers = []
            list_even_numbers = []
            if number_type == 'odd':
                for element in list_numbers[::-1]:
                    if element % 2 != 0:
                        list_odd_numbers.append(element)
                        counter += 1
                        if counter == count:
                            break
                print(list_odd_numbers[::-1])
            elif number_type == 'even':
                for element in list_numbers[::-1]:
                    if element % 2 == 0:
                        list_even_numbers.append(element)
                        counter += 1
                        if counter == count:
                            break
                print(list_even_numbers[::-1])
    command = input()
print(list_numbers)