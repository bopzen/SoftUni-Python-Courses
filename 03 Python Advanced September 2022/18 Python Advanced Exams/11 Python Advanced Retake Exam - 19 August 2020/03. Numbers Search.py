def numbers_searching(*args):
    result = []
    duplicates = []
    last_missing_number = 0
    numbers = args
    for num in range(min(numbers), max(numbers)+1):
        if num not in numbers:
            last_missing_number = num
        if numbers.count(num) > 1:
            duplicates.append(num)
    result.append(last_missing_number)
    result.append(duplicates)
    return result