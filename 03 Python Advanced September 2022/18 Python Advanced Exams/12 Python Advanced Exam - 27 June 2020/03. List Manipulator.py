def list_manipulator(numbers, *args):
    args_list = []
    for element in args:
        args_list.append(element)
    action = args_list.pop(0)
    direction = args_list.pop(0)
    if action == 'remove':
        if args_list:
            if direction == 'beginning':
                for _ in range(args_list[0]):
                    numbers.pop(0)
            elif direction == 'end':
                for _ in range(args_list[0]):
                    numbers.pop()
        else:
            if direction == 'beginning':
                numbers.pop(0)
            elif direction == 'end':
                numbers.pop()
    elif action == 'add':
        if direction == 'beginning':
            for element in reversed(args_list):
                numbers.insert(0, element)
        if direction == 'end':
            for element in args_list:
                numbers.append(element)
    return numbers