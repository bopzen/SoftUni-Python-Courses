list_memory_elements = input().split()
moves = 0
while True:
    command = input()
    if command == 'end':
        break
    moves += 1
    list_command = command.split()
    index1 = int(list_command[0])
    index2 = int(list_command[1])
    if index1 == index2 or index1 < 0 or index1 >= len(list_memory_elements) or index2 < 0 or index2 >= len(list_memory_elements):
        print("Invalid input! Adding additional elements to the board")
        add_element = str(-moves) + 'a'
        half = len(list_memory_elements) // 2
        list_memory_elements.insert(half, add_element)
        list_memory_elements.insert(half, add_element)
    else:
        if list_memory_elements[index1] == list_memory_elements[index2]:
            print(f"Congrats! You have found matching elements - {list_memory_elements[index1]}!")
            if index1 > index2:
                list_memory_elements.pop(index1)
                list_memory_elements.pop(index2)
            else:
                list_memory_elements.pop(index2)
                list_memory_elements.pop(index1)
        else:
            print("Try again!")
    if len(list_memory_elements) == 0:
        print(f"You have won in {moves} turns!")
        break
if command == 'end':
    print("Sorry you lose :(")
    print(" ".join(list_memory_elements))


