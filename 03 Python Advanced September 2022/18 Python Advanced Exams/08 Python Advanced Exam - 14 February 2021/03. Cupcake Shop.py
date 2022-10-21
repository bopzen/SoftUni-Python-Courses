def stock_availability(inventory, operation, *args):
    if operation == 'delivery':
        for arg in args:
            inventory.append(arg)
    elif operation == 'sell':
        if args:
            for arg in args:
                if type(arg) == int:
                    for _ in range(int(arg)):
                        inventory.pop(0)
                else:
                    while arg in inventory:
                        inventory.remove(arg)
        else:
            inventory.pop(0)
    return inventory