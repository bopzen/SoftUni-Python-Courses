def best_list_pureness(*args):
    best_pureness = -10000000
    best_rotation = 0
    numbers = args[0]
    k = args[1]
    for rotation in range(k+1):
        pureness = 0
        for i in range(len(numbers)):
            pureness += numbers[i] * i
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation
        numbers.insert(0, numbers.pop())
        print(rotation)
        print(pureness)
        print(numbers)
    return f"Best pureness {best_pureness} after {best_rotation} rotations"