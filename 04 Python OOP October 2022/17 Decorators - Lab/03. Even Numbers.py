def even_numbers(function):
    def wrapper(numbers):
        result = function(numbers)
        even = [x for x in result if x % 2 == 0]
        return even
    return wrapper