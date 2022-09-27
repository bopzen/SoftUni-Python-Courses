def even_odd(*args):
    command = args[-1]
    result = []
    if command == 'even':
        result = list(filter(lambda x: x % 2 == 0, args[:-1]))
    elif command == 'odd':
        result = list(filter(lambda x: x % 2 != 0, args[:-1]))
    return result